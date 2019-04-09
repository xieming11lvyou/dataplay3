from dataplay.mlsvc.job import MLJobStatus
from dataplay.mlsvc.time_serials import TimeSerialsForecastsJob
from dataplay.datasvc.manager import DatasetManager


def test_job_time_serials():
    dataset_id = 'nasdaq'
    dataset = DatasetManager.get_dataset(dataset_id)
    assert dataset is not None
    df = dataset.get_df()
    assert df is not None

    features = ['Date']
    targets = ['Open']

    job_option = {}

    job = TimeSerialsForecastsJob(
        'testtimeserials', dataset_id, features, targets, job_option
    )
    job.train()

    predict_result = job.predict(df[features])
    assert job.get_status() == MLJobStatus.SUCCESS
    # predict_result.to_csv('/tmp/classification.csv', encoding='utf-8')
    job.clean()
