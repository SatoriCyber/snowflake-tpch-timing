import snowflake.connector
import time

satori_con = snowflake.connector.connect(
    user='<YOUR USERNAME>',
    password='<YOUR PASSWORD>',
    account='<YOUR SNOWFLAKE ACCOUNT>',
    host='<YOUR SATORI HOSTNAME>',
    database='snowflake_sample_data',
    schema='tpch_sf1',
    warehouse='<YOUR VIRTUAL DATA WAREHOUSE>'
)

direct_con = snowflake.connector.connect(
    user='<YOUR USERNAME>',
    password='<YOUR PASSWORD>',
    account='<YOUR SNOWFLAKE ACCOUNT>',
    database='snowflake_sample_data',
    schema='tpch_sf1',
    warehouse='<YOUR VIRTUAL DATA WAREHOUSE>'
)

NUM_OF_SAMPLES = 100


def benchmark(with_satori: bool):
    if with_satori:
        print("Benchmarking with Satori!")
    else:
        print("Benchmarking without Satori")

    filename = "results_with_satori.txt" if with_satori else "results_without_satori.txt"
    with open(filename, 'w') as result_file:
        with open('tpch.sql') as f:
            all_queries = f.read()
            results = "Test\tTime\n"
            for i in range(0, NUM_OF_SAMPLES):

                # Running the benchmark for each query in the queries file
                for query in all_queries.split(';'):
                    label = query.split("-- ")[1].split('\n')[0]
                    query = query.rstrip()
                    start_ts = time.time()

                    cs = satori_con.cursor() if with_satori else direct_con.cursor()
                    cs.execute(query)
                    rows = cs.fetchall()
                    for _row in rows:
                        continue

                    end_ts = time.time()
                    delta = end_ts-start_ts

                    # Results are tab-delimited for easy pasting to a spreadsheet
                    results += "{0:s}\t{1:3.5f}\n".format(label, delta)
            result_file.write(results)


if __name__ == '__main__':
    # Running benchmarks without Satori
    benchmark(False)

    # Running benchmarks with Satori
    benchmark(True)
