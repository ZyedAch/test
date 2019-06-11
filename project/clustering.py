import logging
import datetime
from project.utils.config import extract_json, df_formatting
from sklearn.cluster import KMeans
import os

logger = logging.getLogger(__name__)


def build_clustering(outdir, input_file):
    """

    :param outdir: output directory
    :param input_file: input data (for example : Brisbane_CityBike.json)
    :return: none
    """

    # data extraction & formatting
    logger.info('start at {date}'.format(date=format(datetime.datetime.today(), "%d/%m/%Y-%H:%M:%S")))

    df = extract_json(input_file)
    final_df = df_formatting(df)

    # clusters creation
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(final_df[['latitude', 'longitude']])
    final_df['clusters'] = kmeans.predict(final_df[['latitude', 'longitude']])

    # let's save our result
    logger.info('save clusters')

    filename = '{date}_results.csv'.format(date=format(datetime.datetime.today(), "%Y%m%d-%H%M%S"))
    filepath = os.path.join(outdir, filename)
    final_df[['id', 'clusters']].to_csv(filepath, sep=';', index=False)

    logger.info('job done at {date}'.format(date=format(datetime.datetime.today(), "%d/%m/%Y-%H:%M:%S")))


if __name__ == '__main__':
    build_clustering(outdir='../output/',
                     input_file='../Brisbane_CityBike.json')
