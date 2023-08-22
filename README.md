# OpenAI API Quickstart - Python example app

This is an example of a fusion between xChips and the OpenAI API. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the [quickstart tutorial](https://beta.openai.com/docs/quickstart) for original pet name creator example.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Check your [OpenAI API account](https://platform.openai.com/account/billing/overview). OpenAI API is not free!

9. Add your MQTT Topic to the `.env` file, typically `x/data/sdg/<chipid>`.

10. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
