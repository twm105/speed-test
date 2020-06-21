import speedtest
import datetime as dt
import csv


results_file = 'speedtest_results.csv'


def run_speedtest():
    ''' Function that runs a speedtest (speedtest-cli) and returns the download and upload speeds in bit/s and ping in ms.
    Tom Maisey, June 2020 '''

    st = speedtest.Speedtest()
    st.get_servers()
    st.get_best_server()
    st.download()
    st.upload()
    results = st.results.dict()
    return results['download'], results['upload'], results['ping']


def main():

    dl, ul, ping = run_speedtest()
    with open(results_file, 'a') as res:
        writer = csv.writer(res)
        writer.writerow([dt.datetime.now(), dl, ul, ping])


if __name__ == '__main__':
    main()