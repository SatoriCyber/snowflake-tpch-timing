# TPC-H Snowflake Benchmark
This is a benchmarking test of TPC-H queries on Snowflake (using the TPC-H datasets available in Snowflake), to be executed with and without Satori.

## Required packages installation
```bash
pip3 install -r requirements.txt
```

## Changes (prior to execution)
Change the settings in satori_con and direct_con to match the settings of your account.

If you do not already have a Satori account, you can either apply for one, or if you want to just benchmark your SF account, delete / comment out the Satori test:
```benchmark(True)```

If you feel like changing the number of iterations, you can change the ```NUM_OF_SAMPLES``` constant (default is 100).

to execute, simply run the:
```python3 perftest.py```
