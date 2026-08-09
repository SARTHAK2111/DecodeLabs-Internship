"""
DecodeLabs - Project 3
AI Recommendation Logic

A simple recommendation system that:
1. Takes user interests as input
2. Matches those interests with item attributes
3. Calculates a similarity score
4. Displays the most relevant recommendations
"""


# --------------------------------------------------
# 1. SAMPLE ITEMS
# --------------------------------------------------

items = [
    {
        "name": "The Matrix",
        "category": "movie",
        "interests": {"action", "sci-fi", "thriller"}
    },
    {
        "name": "Interstellar",
        "category": "movie",
        "interests": {"sci-fi", "space", "adventure"}
    },
    {
        "name": "Inception",
        "category": "movie",
        "interests": {"action", "sci-fi", "thriller"}
    },
    {
        "name": "The Office",
        "category": "series",
        "interests": {"comedy", "workplace", "sitcom"}
    },
    {
        "name": "Friends",
        "category": "series",
        "interests": {"comedy", "friendship", "sitcom"}
    },
    {
        "name": "Planet Earth",
        "category": "documentary",
        "interests": {"nature", "animals", "science"}
    },
    {
        "name": "Avengers",
        "category": "movie",
        "interests": {"action", "superhero", "adventure"}
    }
]


# --------------------------------------------------
# 2. RECOMMENDATION FUNCTION
# --------------------------------------------------

def calculate_similarity(user_interests, item_interests):
    """
    Calculate similarity between user preferences
    and an item's interests.

    The score represents the number of matching
    interests.
    """

    matching_interests = user_interests.intersection(item_interests)

    return len(matching_interests), matching_interests


# --------------------------------------------------
# 3. GET USER INPUT
# --------------------------------------------------

print("=" * 50)
print("       DecodeLabs AI Recommendation System")
print("=" * 50)

print("\nAvailable interests:")
print("action, sci-fi, thriller, space, adventure")
print("comedy, workplace, sitcom, friendship")
print("nature, animals, science, superhero")

user_input = input(
    "\nEnter your interests separated by commas: "
)

# Convert input into a set
user_interests = {
    interest.strip().lower()
    for interest in user_input.split(",")
    if interest.strip()
}


# --------------------------------------------------
# 4. FIND RECOMMENDATIONS
# --------------------------------------------------

recommendations = []

for item in items:

    score, matching_interests = calculate_similarity(
        user_interests,
        item["interests"]
    )

    if score > 0:
        recommendations.append(
            {
                "name": item["name"],
                "category": item["category"],
                "score": score,
                "matching_interests": matching_interests
            }
        )


# --------------------------------------------------
# 5. SORT BY SIMILARITY SCORE
# --------------------------------------------------

recommendations.sort(
    key=lambda item: item["score"],
    reverse=True
)


# --------------------------------------------------
# 6. DISPLAY RESULTS
# --------------------------------------------------

print("\n" + "=" * 50)
print("              RECOMMENDATIONS")
print("=" * 50)

if recommendations:

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        print(f"\n{index}. {recommendation['name']}")
        print(f"   Category: {recommendation['category']}")
        print(f"   Similarity Score: {recommendation['score']}")
        print(
            "   Matching Interests:",
            ", ".join(
                recommendation["matching_interests"]
            )
        )

else:

    print(
        "\nNo matching recommendations found."
    )

print("\nThank you for using the recommendation system!")