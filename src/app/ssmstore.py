import boto3

ssm = boto3.client("ssm")

def fetch_ssm_parm(param_key :str) -> str:
    res = ssm.get_parameter(Name=param_key, WithDecryption=True)
    return res["Parameter"]["Value"]