from flask import Flask, render_template, request, redirect, send_file
from scarpper import integrated_get_jobs as get_jobs
from scrap_function.function_save import save_to_file
app = Flask("search_job")

db = {}         # fake db


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/report")
def report():
    word = request.args.get('word')

    if word:
        word = word.lower()

        existing_jobs = db.get(word)   # find it in DB
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs

    else:
        return redirect("/")

    return render_template('report.html',
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs
                           )


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        print(word)
        if not word:
            print("notw")
            raise Exception()       # raise error

        word = word.lower()
        jobs = db.get(word)

        if not jobs:
            print("notj")
            raise Exception()

        save_to_file(jobs)
        return send_file("jobs.csv", attachment_filename="jobs.csv")

    except:
        return redirect("/")


app.run()
