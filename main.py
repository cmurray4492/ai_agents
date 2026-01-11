from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def generate_X_post(topic: str) -> str:
    prompt = f"""
    You are an expert socail media manager and you excel at crafting viral and
    highly engaging posts for X (formerly Twitter).

    Your task is to generate a post that is concise, impactful and tailored to
    the topic provided by the user. Avoid using hashtags and emojis (a few
    emojis are ok but not too many).

    Keep the post short and focused, structure in a clean readable way using
    line breaks and empty lines to enhance readbility.

    Here is ther topic provided by user for which you need to generate a post:
    <topic>
    {topic}
    </topic>

    Here are some examples of topics and generated posts"
    <examples>
        <example-1>
            <topic>
            </topic>

            <generated-post>
            </generated-post>
        </example-1>
        <example-2>
            <topic>
            </topic>

            <generated-post>
            </generated-post>
         </example-2>
    </examples>
    Please use the tone, language, structure, and style of the examples
    provided above to generate a post that is engaging and relevant.
    Don't use the content fromw the examples!
    """
    response = client.responses.create(
        model="gpt-4o",
        input=prompt
        )

    return response.output_text


def main():
    usr_input = input("What should the post be about? ")
    x_post = generate_X_post(usr_input)
    print("Generated X post: ")
    print(x_post)


if __name__ == "__main__":
    main()
