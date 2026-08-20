from predictor import predict_role


resume = """
Python developer experienced in Django,
Flask, REST API, MySQL, PostgreSQL,
Bootstrap, Git and backend development.
"""


result = predict_role(resume)


print(result)