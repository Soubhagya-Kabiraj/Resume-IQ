from .job_data import JOB_RECOMMENDATIONS

def get_recommendations(predicted_role):

    recommendations = JOB_RECOMMENDATIONS.get(
        predicted_role,
        []
    )

    return recommendations