import psycopg2
import time
import matplotlib.pyplot as plt

class QueryAnalyzer:
    def __init__(self, hostname, database, username, password, port=5432):
        self.connection = psycopg2.connect(
            host=hostname, 
            database=database, 
            user=username, 
            password=password, 
            port=port
        )

    def analyze_queries(self, queries):
        """ Analyze the execution time of each query in the provided list of queries and return the times. """
        execution_times = []
        with self.connection:
            with self.connection.cursor() as cursor:
                for query in queries:
                    start_time = time.time()
                    cursor.execute(query)
                    execution_time = time.time() - start_time
                    execution_times.append(execution_time)
                    print(f"Execution time: {execution_time} seconds\n")
        return execution_times

    def plot_execution_times(self, execution_times):
        """ Plot the execution times. """
        plt.figure()
        plt.bar(range(len(execution_times)), execution_times, tick_label=[f"Query {i+1}" for i in range(len(execution_times))])
        plt.xlabel('Queries')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Query Execution Times')
        plt.show()

    def close(self):
        """ Close the database connection. """
        self.connection.close()

hostname = 'localhost'
database = 'exercises'
username = 'postgres'
pwd = '1234'
port_id = 5432

analyzer = QueryAnalyzer(hostname, database, username, pwd, port_id)

queries = [
    "WITH RECURSIVE t(n) AS (VALUES (1) UNION ALL SELECT n+1 FROM t WHERE n < 100) SELECT * FROM t, cd.bookings b WHERE t.n = b.facid",
    
    "WITH split_table AS (SELECT unnest(ARRAY[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) AS array) SELECT * FROM cd.bookings b JOIN split_table s ON s.array = b.facid",

    "SELECT * FROM cd.bookings b WHERE b.facid IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100)",
    
    """
    CREATE TEMP TABLE tmp_table (num INTEGER);
    INSERT INTO tmp_table VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12), (13), (14), (15), (16), (17), (18), (19), (20), (21), (22), (23), (24), (25), (26), (27), (28), (29), (30), (31), (32), (33), (34), (35), (36), (37), (38), (39), (40), (41), (42), (43), (44), (45), (46), (47), (48), (49), (50), (51), (52), (53), (54), (55), (56), (57), (58), (59), (60), (61), (62), (63), (64), (65), (66), (67), (68), (69), (70), (71), (72), (73), (74), (75), (76), (77), (78), (79), (80), (81), (82), (83), (84), (85), (86), (87), (88), (89), (90), (91), (92), (93), (94), (95), (96), (97), (98), (99), (100);
    SELECT * FROM cd.bookings b WHERE b.facid IN (SELECT num FROM tmp_table);

    """
]


execution_times = analyzer.analyze_queries(queries)

analyzer.plot_execution_times(execution_times)

analyzer.close()

