import mysql.connector
from mysql.connector import Error

def get_connection():
    
    try:
        connection = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password= '',
        database= 'academic_resource_manager'
        )

        return connection
    
    except Error as e:
        print(f'Database Error: {e}')
        return None
    
def get_resources(subject_id=None, type_id=None, sort_by="newest"):

    connection = get_connection()

    cursor = connection.cursor()

    query = """SELECT

        r.resource_id,

        r.title,

        s.subject_name,

        rt.type_name,

        u.username,

        r.file_link,

        r.upload_date

        FROM resources r

        JOIN subjects s
        ON r.subject_id = s.subject_id

        JOIN resource_types rt
        ON r.type_id = rt.type_id

        JOIN users u
        ON r.user_id = u.user_id

        WHERE r.status='Approved'"""
    
    params = []

    if subject_id:
        query += " AND r.subject_id = %s"
        params.append(subject_id)
    
    if type_id:
        query += " AND r.type_id = %s"
        params.append(type_id)
    
    if sort_by == "newest":
        query += " ORDER BY r.upload_date DESC"

    elif sort_by == "oldest":
        query += " ORDER BY r.upload_date ASC"

    elif sort_by == "title_asc":
        query += " ORDER BY r.title ASC"

    elif sort_by == "title_desc":
        query += " ORDER BY r.title DESC"

    cursor.execute(query, params)

    resources = cursor.fetchall()

    cursor.close()
    connection.close()

    return resources



def get_subjects():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT subject_id, subject_name
        FROM subjects
    """)

    subjects = cursor.fetchall()

    cursor.close()
    connection.close()

    return subjects


def get_resource_types():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT type_id, type_name
        FROM resource_types
    """)

    resource_types = cursor.fetchall()

    cursor.close()
    connection.close()

    return resource_types

def add_resource(title, description, file_link,
                 subject_id,  type_id, user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO resources
        (
            title,
            description,
            file_link,
            subject_id,
            type_id,
            user_id
        )

        VALUES
        (%s,%s,%s,%s,%s,%s)
          """, (
        title,
        description,
        file_link,
        subject_id,
        type_id,
        user_id
    ))

    connection.commit()

    cursor.close()
    connection.close()

def get_user(username):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, username, password, role
        FROM users
        WHERE username = %s
    """, (username,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user

def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*) AS total,
            COALESCE(SUM(status='Pending'), 0) AS pending,
            COALESCE(SUM(status='Approved'), 0) AS approved,
            COALESCE(SUM(status='Rejected'), 0) AS rejected
        FROM resources
    """)

    stats = cursor.fetchone()

    cursor.close()
    connection.close()

    return stats

def get_resources_by_status(status):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            r.resource_id,
            r.title,
            u.username,
            s.subject_name,
            r.upload_date
        FROM resources r
        JOIN users u
            ON r.user_id = u.user_id
        JOIN subjects s
            ON r.subject_id = s.subject_id
        WHERE r.status = %s
        ORDER BY r.upload_date DESC
    """, (status,))

    resources = cursor.fetchall()

    cursor.close()
    connection.close()

    return resources


def approve_resource(resource_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE resources
        SET status = 'Approved'
        WHERE resource_id = %s
    """, (resource_id,))

    connection.commit()

    cursor.close()
    connection.close()

def reject_resource(resource_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE resources
        SET status='Rejected'
        WHERE resource_id=%s
    """, (resource_id,))

    connection.commit()

    cursor.close()
    connection.close()

def get_user_resources(user_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            r.resource_id,
            r.title,
            s.subject_name,
            rt.type_name,
            r.status,
            r.upload_date
        FROM resources r
        JOIN subjects s
            ON r.subject_id = s.subject_id
        JOIN resource_types rt
            ON r.type_id = rt.type_id
        WHERE r.user_id = %s
        ORDER BY r.upload_date DESC
    """, (user_id,))

    resources = cursor.fetchall()

    cursor.close()
    connection.close()

    return resources


def get_resource_by_id(resource_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            resource_id,       
            title,
            description,
            file_link,
            subject_id,
            type_id,
            status,
            user_id
        FROM resources
        WHERE resource_id = %s
    """, (resource_id,))

    resource = cursor.fetchone()

    cursor.close()
    connection.close()

    return resource

def update_resource(resource_id,
                    title,
                    description,
                    file_link,
                    subject_id,
                    type_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE resources
        SET
            title = %s,
            description = %s,
            file_link = %s,
            subject_id = %s,
            type_id = %s,
            status = 'Pending'
        WHERE resource_id = %s
    """,
    (
        title,
        description,
        file_link,
        subject_id,
        type_id,
        resource_id
    ))

    connection.commit()

    cursor.close()
    connection.close()


def delete_resource(resource_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM resources
        WHERE resource_id = %s
    """, (resource_id,))

    connection.commit()

    cursor.close()
    connection.close()


def get_user_by_username(username):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE username = %s
    """, (username,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def get_user_by_email(email):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE email = %s
    """, (email,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def create_user(username, email, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users
        (username, email, password)
        VALUES (%s, %s, %s)
    """,
    (
        username,
        email,
        password
    ))

    connection.commit()

    cursor.close()
    connection.close()




if __name__ == '__main__':
    connection = get_connection()
    