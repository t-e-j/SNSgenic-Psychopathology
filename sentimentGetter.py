import textblob
from multiprocessing import Pool, cpu_count, Process, Pipe
from multiprocessing.pool import ThreadPool
import random
import os
import cPickle as pickle
import sqlite3
from collections import namedtuple

Result = namedtuple("Result", ['db_id', 'author', 'sentiment', 'subjectivity'])

def fill_thread_queue(dbpath, queue_size, authors, outpipe):
    conn = sqlite3.connect(dbpath)
    conn.execute("pragma journal_mode=wal")
    cursor = conn.cursor()
    thread_queue = []
    last_queue_size = 0
    while thread_queue.__sizeof__() < queue_size and authors:
        curr_queue_size = thread_queue.__sizeof__()
        if curr_queue_size > last_queue_size:
            print "Queue size: %d" % (curr_queue_size,)
            last_queue_size = curr_queue_size
        author = authors.pop()
        query = "SELECT db_id,author,body FROM comments WHERE author='%s'" % (author)
        thread_queue += list(cursor.execute(query))
    with open("unprocessedAuthors.pickle","w") as f : pickle.dump(authors,f)
    conn.close()
    outpipe.send(tuple(thread_queue))
    outpipe.send(authors)

class Writer:
    def __init__(self):
        self.counter = 1
    def resultsGen(self):
        files = os.listdir("pickles/")
        for path in files:
            with open("pickles/%s" % (path,),"r") as file: results = pickle.load(file)
            for result in results:
                yield result
    def write_results(self,results):
        name = "pickles/results%d" % (self.counter,)
        self.counter+=1
        with open(name,"w") as f : pickle.dump(results, f)
        return "success"
    def commit_results(self, dbpath):
        results = self.resultsGen()
        conn = sqlite3.connect(dbpath)
        cursor = conn.cursor()
        for result in results:
            cursor.execute("UPDATE comments SET textblob_sentiment = %f, subjectivity = %f WHERE db_id = %d" %
                           (result.sentiment, result.subjectivity, result.db_id))
        conn.commit()
        conn.close()

def score(fields):
    db_id, author, body = fields
    body = textblob.TextBlob(body)
    return Result(db_id=db_id,
                  author=author,
                  sentiment = body.sentiment.polarity,
                  subjectivity = body.subjectivity)

def main_loop(dbpath, to_process, authors):
    print "Initializing thread pool..."
    thread_pool = ThreadPool(processes=2)
    print "Initializing core pool"
    core_pool = Pool(cpu_count() - 2)
    writer = Writer()
    async_writer = object()
    async_writer = thread_pool.apply_async("Initializing".__str__)
    loop_counter = 1
    while to_process:
        print "Loop %d" % (loop_counter,)
        iPipe, oPipe = Pipe()
        queue_proc = Process(target=fill_thread_queue,args=(dbpath, 10 ** 7, authors, oPipe))
        queue_proc.start()
        print "Farming out..."
        results = core_pool.map(score, to_process)
        print "Parallel cycle completed"
        print "Writer results : " + async_writer.get()
        async_writer = thread_pool.apply_async(writer.write_results, (results,))
        to_process = iPipe.recv()
        authors = iPipe.recv()
        loop_counter+=1
    print "Writing results to database"
    writer.commit_results(dbpath)

def main(dbpath):
    #conn = sqlite3.connect(dbpath)
    #c = conn.cursor()
    #print "Identifying distinct authors"
    #authors = [x[0] for x in c.execute("SELECT DISTINCT(author) FROM comments")]
    #random.shuffle(authors)
    #conn.close()
    with open("authors.pickle","r") as f : authors = pickle.load(f)
    print "Initializing queue"
    iPipe, oPipe = Pipe()
    queue_proc = Process(target=fill_thread_queue, args=(dbpath, 10 ** 7, authors, oPipe))
    queue_proc.start()
    to_process = iPipe.recv()
    authors = iPipe.recv()
    print "Entering main loop"
    main_loop(dbpath, to_process, authors)


if __name__ == "__main__":
    print "Enter main"
    main("comments.db")
