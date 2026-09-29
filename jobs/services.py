import re


def calculate_skills_match(job, profile):
    """
    Calculate the percentage of required job skills
    that match the job seeker's skills.
    """

    required_skills = {
        skill.strip().lower()
        for skill in job.required_skills.split(",")
        if skill.strip()
    }

    user_skills = {
        skill.strip().lower()
        for skill in profile.skills.split(",")
        if skill.strip()
    }

    if not required_skills:
        return 0

    matched_skills = required_skills.intersection(user_skills)

    return (
        len(matched_skills) / len(required_skills)
    ) * 100


def calculate_experience_match(job, profile):
    """
    Calculate experience match using years of experience.
    """

    required_text = job.experience_required.strip().lower()
    user_text = profile.experience.strip().lower()

    if not required_text:
        return 100

    if not user_text:
        return 0

    user_match = re.search(
    r"\d+(?:\.\d+)?",
    user_text
    )

    if not user_match:
        return 0

    user_years = float(user_match.group())

    required_numbers = re.findall(
    r"\d+(?:\.\d+)?",
    required_text
    )

    if not required_numbers:
        return 0

    required_years = [
        float(number)
        for number in required_numbers
    ]

    if len(required_years) >= 2:

        minimum_years = min(required_years)
        maximum_years = max(required_years)

        if minimum_years <= user_years <= maximum_years:
            return 100

        if user_years >= minimum_years:
            return 100

        return 0

    required_years = required_years[0]

    if user_years >= required_years:
        return 100

    return 0


def calculate_location_match(job, profile):
    """
    Calculate the location match between a job
    and a job seeker's preferred location.
    """

    job_location = (
        job.location
        .strip()
        .lower()
        .replace(" ", "")
    )

    preferred_location = (
        profile.preferred_location
        .strip()
        .lower()
        .replace(" ", "")
    )

    if not preferred_location:
        return 0

    if job_location == preferred_location:
        return 100

    if preferred_location in job_location:
        return 100

    if job_location in preferred_location:
        return 100

    return 0


def calculate_job_type_match(job, profile):
    """
    Calculate the employment type match between a job
    and the job seeker's preferred job type.
    """

    job_type = (
        job.get_employment_type_display()
        .strip()
        .lower()
    )

    preferred_type = (
        profile.preferred_job_type
        .strip()
        .lower()
    )

    if not preferred_type:
        return 0

    if job_type == preferred_type:
        return 100

    return 0


def calculate_job_match(job, profile):
    """
    Calculate the overall job match score.
    """

    skills_score = calculate_skills_match(
        job,
        profile
    )

    experience_score = calculate_experience_match(
        job,
        profile
    )

    location_score = calculate_location_match(
        job,
        profile
    )

    job_type_score = calculate_job_type_match(
        job,
        profile
    )

    final_score = (
        skills_score * 0.50
        + experience_score * 0.20
        + location_score * 0.15
        + job_type_score * 0.15
    )

    return round(final_score, 2)