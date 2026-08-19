import json
import random
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

PROFILE_PATH = BASE_DIR / "data" / "learning_profile.json"
CURRICULUM_PATH = BASE_DIR / "data" / "curriculum.json"
HISTORY_PATH = BASE_DIR / "data" / "learning_history.json"


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_profile():
    return load_json(PROFILE_PATH)


def load_curriculum():
    return load_json(CURRICULUM_PATH)


def load_history():
    return load_json(HISTORY_PATH)


def choose_domain(profile, history):
    domains = profile["domains"]

    recent_domains = [
        lesson["domain"]
        for lesson in history["lessons"][-3:]
    ]

    candidates = {
        domain: config["weight"]
        for domain, config in domains.items()
        if domain not in recent_domains
    }

    if not candidates:
        candidates = {
            domain: config["weight"]
            for domain, config in domains.items()
        }

    return random.choices(
        list(candidates.keys()),
        weights=list(candidates.values()),
        k=1,
    )[0]


def choose_content_type(profile):
    content_types = profile["content_types"]

    return random.choices(
        list(content_types.keys()),
        weights=[
            config["weight"]
            for config in content_types.values()
        ],
        k=1,
    )[0]


def choose_topic(domain, content_type, curriculum, history):
    available_topics = curriculum[domain][content_type]

    used_topics = {
        lesson["topic"]
        for lesson in history["lessons"]
        if lesson["domain"] == domain
    }

    unused_topics = [
        topic
        for topic in available_topics
        if topic not in used_topics
    ]

    if not unused_topics:
        unused_topics = available_topics

    return random.choice(unused_topics)


def create_lesson_spec():
    profile = load_profile()
    curriculum = load_curriculum()
    history = load_history()

    domain = choose_domain(profile, history)
    content_type = choose_content_type(profile)
    topic = choose_topic(
        domain,
        content_type,
        curriculum,
        history,
    )

    duration = random.randint(3, profile["constraints"]["max_duration_minutes"])

    return {
        "domain": domain,
        "learning_type": content_type,
        "topic": topic,
        "difficulty": "intermediate",
        "duration_minutes": duration,
    }


if __name__ == "__main__":
    lesson = create_lesson_spec()

    print("Next lesson:")
    print(json.dumps(lesson, indent=2))

def save_lesson_to_history(lesson_spec):
    history = load_history()

    history["lessons"].append(lesson_spec)

    with open(HISTORY_PATH, "w", encoding="utf-8") as file:
        json.dump(
            history,
            file,
            indent=2,
            ensure_ascii=False,
        )