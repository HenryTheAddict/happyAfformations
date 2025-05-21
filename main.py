import random

positive_words = ["Not a mean person", "not mean", "WEAK", "EVIL", "Incapable", "normal", "mingjingled"]
emojis = ["🌟", "💪", "🌈", "😊", "💖", "💅","💘", "💗", "🌺","😈", '🤣', "🍁", "(emoji)"]
affirmations = [
    "You are kind and not mean.",
    "You are very nice to others.",
    "You should be not evil.",
    "You are NOT Zesty.",
    'You dont reply "k" to messages.',
    'You are not like finley.',
    'You aiafeeakdfsdda.',
    'You are a freaky goblin.',
    'You DONT.',
    'You NEED afformations to live.',
    "You. dont. use. periods. to. end. your. sentances."
]

def generate_affirmation(name=""):
  """Generates a personalized affirmation."""
  adj = random.choice(positive_words)
  emoji = random.choice(emojis)
  affirmation = random.choice(affirmations)
  if name:
    return f"{name}, you are {adj}! {emoji} {affirmation}"
  return f"You are {adj}! {emoji} {affirmation}"

# Example usage
print(generate_affirmation("test"))
print(generate_affirmation())
