from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from database import (
    get_resources,
    get_subjects,
    get_resource_types,
    add_resource,
    get_user,
    get_dashboard_stats,
    get_resources_by_status,
    approve_resource,
    reject_resource,
    get_user_resources,
    get_resource_by_id,
    update_resource,
    delete_resource,
    get_user_by_username,
    get_user_by_email,
    create_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

app.secret_key = "academic_resource_manager_secret"

@app.route("/")
def home():

    subjects = get_subjects()
    resource_types = get_resource_types()

    return render_template(
    "home.html",
    subjects=subjects,
    resource_types=resource_types
    )

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/resources")
def resources():

    subject_id = request.args.get("subject")
    type_id = request.args.get("type")
    sort_by = request.args.get("sort", "newest")

    resources = get_resources(subject_id, type_id, sort_by)

    subjects = get_subjects()
    resource_types = get_resource_types()

    return render_template(
        "resources.html",
        resources=resources,
        subjects=subjects,
        resource_types=resource_types,
        selected_subject=subject_id,
        selected_type=type_id,
        selected_sort=sort_by
    )

@app.route("/add_resources", methods=["GET", "POST"])
def add_resources():

    if "user_id" not in session:
        return redirect(url_for("login"))

    subjects = get_subjects()
    resource_types = get_resource_types()

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        file_link = request.form["file_link"]

        subject_id = request.form["subject_id"]
        type_id = request.form["type_id"]
        user_id = session["user_id"]

        add_resource(
                title,
                description,
                file_link,
                subject_id,
                type_id,
                user_id
                )
        
        return redirect(url_for("resources"))

    return render_template(
           "add_resources.html",
           subjects=subjects,
           resource_types=resource_types,
           resource=None
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username)

        if user is None:
            return render_template(
                   "login.html",
                   error="User does not exist."
                )

        if not check_password_hash(user[2], password):
            return render_template(
                  "login.html",
                  error="Incorrect password."
                )

        session["user_id"] = user[0]
        session["username"] = user[1]
        session["role"] = user[3]

        return redirect(url_for("home"))
    
    return render_template('login.html')

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


@app.route("/admin")
def admin_dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if session["role"] != "admin":
        return redirect(url_for("home"))

    stats = get_dashboard_stats()

    return render_template(
           "admin_dashboard.html",
           stats=stats
        )

@app.route("/admin/manage_resources")
def manage_resources():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if session["role"] != "admin":
        return redirect(url_for("home"))

    pending = get_resources_by_status("Pending")
    approved = get_resources_by_status("Approved")
    rejected = get_resources_by_status("Rejected")

    return render_template(
        "manage_resources.html",
        pending=pending,
        approved=approved,
        rejected=rejected
    )


@app.route("/approve_resource/<int:resource_id>")
def approve(resource_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if session["role"] != "admin":
        return redirect(url_for("home"))

    approve_resource(resource_id)

    return redirect(url_for("manage_resources"))

@app.route("/reject_resource/<int:resource_id>")
def reject(resource_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if session["role"] != "admin":
        return redirect(url_for("home"))

    reject_resource(resource_id)

    return redirect(url_for("manage_resources"))


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    resources = get_user_resources(session["user_id"])

    return render_template(
        "dashboard.html",
        resources=resources
    )


@app.route("/edit_resource/<int:resource_id>", methods=["GET", "POST"])
def edit_resource(resource_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    resource = get_resource_by_id(resource_id)

    if resource is None:
        return redirect(url_for("dashboard"))

    # Make sure the logged-in user owns this resource
    if resource[7] != session["user_id"]:
        return redirect(url_for("dashboard"))

    subjects = get_subjects()
    resource_types = get_resource_types()

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        file_link = request.form["file_link"]
        subject_id = request.form["subject_id"]
        type_id = request.form["type_id"]

        update_resource(
            resource_id,
            title,
            description,
            file_link,
            subject_id,
            type_id
        )

        return redirect(url_for("dashboard"))

    return render_template(
        "add_resources.html",
        resource=resource,
        subjects=subjects,
        resource_types=resource_types
    )


@app.route("/delete_resource/<int:resource_id>")
def delete_resource_route(resource_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    resource = get_resource_by_id(resource_id)

    if resource is None:
        return redirect(url_for("dashboard"))

    if (
        resource[7] != session["user_id"]
        and session["role"] != "admin"
    ):
        return redirect(url_for("dashboard"))

    delete_resource(resource_id)

    if session["role"] == "admin":
        return redirect(url_for("manage_resources"))

    return redirect(url_for("dashboard"))

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if get_user_by_username(username):
            return render_template(
                "register.html",
                error="Username already exists."
            )

        if get_user_by_email(email):
            return render_template(
                "register.html",
                error="Email already exists."
            )

        if password != confirm_password:
            return render_template(
                "register.html",
                error="Passwords do not match."
            )

        hashed_password = generate_password_hash(password)

        create_user(
            username,
            email,
            hashed_password
        )

        return redirect(url_for("login"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)