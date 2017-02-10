#!/usr/bin/env python


import requests
import json


def parse_status(input_json):

    print("in get_status {}".format(input_json))

    print(input_json[0]["id"])
    print(input_json[0]["status"])


    return input_json[0]["status"]

def project_build_status():

    test_url = "https://vwgit.viawest.net/api/v3/projects/105/pipelines?private_token=y7mQWnHaFGFhiGhSKc9S"

    print("in try catch for python call to get rest data for pipeline builds...")

    resp = requests.get(test_url)

    if resp.status_code != 200:

        raise ValueError('GET /105/pipelines {}'.format(resp.status_code))

    print("Call responded with 200 for GET pipelines for project 105")
    print(resp)
    print(resp.json())

    val = parse_status(resp.json())

    print("******  Latest status from pipeline for project 105 is {} *******".format(val))


def main():

    try:
        project_build_status()

    except Exception as inst:
        print("EXCEPTION OCCURED IN CALL to git pipeline monitor...")
        print(type(inst))
        print(inst.args)
        print(inst)


if __name__ == "__main__":
    main()
