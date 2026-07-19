# Academic Resource Management System (ARMS)

A Database Management System Lab project built for Metropolitan University's CSE department.

**Submitted to:** Shrabanti Chowdhury, Lecturer, Department of CSE, Metropolitan University

**Submitted by:**
| Name | Student ID |
|------|------------|
| Md. Fardin Mahtab Nihal Khan | 242-115-206 |
| Syed Ehsan Hussan | 242-115-221 |

**Course:** CSE 224 – Database Management System Lab | **Section:** E | **Batch:** 61st

---

## What is ARMS?

ARMS is a web app that gives students a shared place to upload, organize, and browse academic resources like notes, slides, past papers, whatever helps a course make more sense. Instead of resources being scattered across group chats, drives, and random Facebook posts that get buried in a day, everything lives in one place, sorted by subject and resource type, with an admin checking submissions before they go public so the quality actually stays decent instead of turning into a dumping ground.

Beyond the practical use, the project itself is really about applying what we learned in the DBMS Lab course — relational schema design, SQL, authentication, and full CRUD operations in something that actually works end to end, rather than staying a diagram on paper. It was also a chance to see how the pieces we studied separately (normalization, foreign keys, joins, transactions) actually behave once they're wired into a real backend that real users interact with, instead of isolated exercises in a lab sheet.

## Why we built it

- Give students one central place to find and share course materials, instead of hunting through five different group chats
- Put relational database concepts into practice on a system that's actually used, not just a schema diagram
- Keep resources organized by subject and type instead of scattered everywhere
- Let students contribute their own materials and build something collectively useful
- Keep quality in check through admin review, so the platform doesn't fill up with junk or duplicate uploads
- Keep the interface simple enough that nobody needs a manual to figure out how to upload a PDF

## Who uses it

**Students** can register, log in, upload resources, edit or delete their own submissions (as long as they're still pending or have been rejected — approved ones are locked from the student's side), and browse everything that's been approved. Browsing supports filtering by subject or resource type and sorting results, and there's a personal dashboard where a student can track exactly where each of their uploads stands — pending, approved, or rejected — without having to ask an admin directly.

**Admins** get a dashboard with platform statistics (things like how many resources exist, how many are pending, how many students are active), a queue of pending submissions to approve or reject, and the ability to re-review resources that were already approved if something turns out to be wrong or outdated later. Rather than deleting an approved resource outright when a problem comes up, an admin can send it back to "rejected" instead — that way the original contributor gets a chance to fix and resubmit their work rather than losing it completely. It's a small design choice, but it keeps the system from feeling punitive toward students who made an honest mistake.

## How a submission moves through the system

```
Student uploads a resource
            │
            ▼
      Pending review
            │
            ▼
      Admin reviews it
      ┌───────────────┐
      │               │
   Approved        Rejected
                       │
                       ▼
                Student edits
                       │
                       ▼
               Back to pending
```

Every resource starts in "pending" the moment it's uploaded — nothing goes live automatically. From there an admin either approves it, which makes it publicly browsable, or rejects it, which sends it back to the student with the option to edit and resubmit. That loop can repeat as many times as needed until the resource is in good enough shape to approve.

## Core features

**Authentication** — registration, secure login, hashed passwords (nothing stored in plain text), and role-based access so students and admins see completely different dashboards and permissions

**Resource management** — upload, edit, delete on the student side, plus approval and rejection controls on the admin side, with status tracked at every step

**Browsing** — only approved resources show up publicly, and they can be filtered by subject and resource type, sorted, and each listing shows who contributed it

**Student dashboard** — a personal view of everything you've uploaded, current approval status for each item, the ability to edit anything that got rejected, and deletion for anything still pending or rejected

**Admin dashboard** — platform-wide statistics, a moderation queue for pending submissions, and full management access over every resource in the system, approved or not

## Database

Built on **MySQL**, with four main tables: Users, Resources, Subjects, and Resource Types. Foreign keys tie everything together — each resource is linked back to the user who uploaded it, the subject it belongs to, and its resource type — which keeps the data consistent and avoids repeating information across tables. This was also where a lot of the actual DBMS Lab coursework came in: designing the schema, deciding on the right normal form, and making sure constraints actually enforced the relationships instead of just relying on the application layer to behave.

## Tech stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** MySQL
- **Tools:** VS Code, Git, MySQL Server

## Project structure

```
AcademicResourceManager
│
├── Backend
│   │
│   ├── app.py
│   ├── database.py
│   ├── requirements.txt
│   │
│   ├── static
│   │   ├── css
│   │   └── images
│   │
│   ├── templates
│   │
│   └── Database
│       ├── create_database.sql
│       ├── insert_sample_data.sql
│       └── queries.sql
│
├── Docs
│   └── Project Proposal.pdf
│
├── .gitignore
│
└── README.md
```

## Getting it running

Clone the repo and move into the backend folder:

```bash
git clone <repository-url>
cd Backend
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then set up the database by running `create_database.sql` to create the schema, followed by `insert_sample_data.sql` to load in some sample data so the app isn't empty on first run.

Finally, start the app:

```bash
python app.py
```

Once it's running, you should be able to register a student account, log in, and start uploading — or log in as an admin to review whatever gets submitted.

## Docs

The original project proposal from the planning phase is in the `Docs` folder if you want the fuller background on how this all came together before any code was written.

## What we took away from this

This project ended up being a pretty solid hands-on run-through of relational database design, writing real SQL instead of textbook examples, CRUD operations, normalization, authentication, and role-based authorization — all tied together with Flask on the backend and a working frontend on top. It's one thing to learn these concepts separately in lecture slides, and a pretty different thing to make them all work together in a system that a real user could actually open, use, and break in unexpected ways. Debugging things like foreign key constraints failing silently, or figuring out why a query returned duplicate rows because of a bad join, taught us more about how databases actually behave than any of the lab exercises did on their own.

## Where this could go next

A few things we'd want to add if we kept working on this beyond the course:

- Actual file uploads instead of relying on external links
- Ratings and reviews on resources, so students can flag what's actually useful
- Download stats, to see which resources get used the most
- Better search instead of just filtering by subject/type
- Email notifications when a submission gets approved or rejected
- User profiles with upload history and stats
- A properly mobile-responsive layout, since right now it's built with desktop use in mind

---

**Department of Computer Science & Engineering, Metropolitan University**