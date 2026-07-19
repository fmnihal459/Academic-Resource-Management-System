-- ============================================================
-- Academic Resource Management System
-- Sample SQL Queries
-- ============================================================


-- ============================================================
-- VIEW TABLES
-- ============================================================

SELECT * FROM users;

SELECT * FROM subjects;

SELECT * FROM resource_types;

SELECT * FROM resources;


-- ============================================================
-- USER LOGIN
-- ============================================================

SELECT
    user_id,
    username,
    password,
    role
FROM users
WHERE username = 'sample_username';


-- ============================================================
-- CHECK USERNAME EXISTS
-- ============================================================

SELECT *
FROM users
WHERE username = 'sample_username';


-- ============================================================
-- CHECK EMAIL EXISTS
-- ============================================================

SELECT *
FROM users
WHERE email = 'sample@email.com';


-- ============================================================
-- VIEW ALL SUBJECTS
-- ============================================================

SELECT
    subject_id,
    subject_name
FROM subjects;


-- ============================================================
-- VIEW ALL RESOURCE TYPES
-- ============================================================

SELECT
    type_id,
    type_name
FROM resource_types;


-- ============================================================
-- DISPLAY APPROVED RESOURCES
-- ============================================================

SELECT

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

WHERE r.status='Approved'

ORDER BY r.upload_date DESC;


-- ============================================================
-- FILTER BY SUBJECT
-- ============================================================

SELECT

    r.resource_id,

    r.title,

    s.subject_name

FROM resources r

JOIN subjects s
ON r.subject_id = s.subject_id

WHERE r.subject_id = 1
AND r.status='Approved';


-- ============================================================
-- FILTER BY RESOURCE TYPE
-- ============================================================

SELECT

    r.resource_id,

    r.title,

    rt.type_name

FROM resources r

JOIN resource_types rt
ON r.type_id = rt.type_id

WHERE r.type_id = 1
AND r.status='Approved';


-- ============================================================
-- VIEW USER'S OWN RESOURCES
-- ============================================================

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

WHERE r.user_id = 1

ORDER BY r.upload_date DESC;


-- ============================================================
-- GET SINGLE RESOURCE
-- ============================================================

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

WHERE resource_id = 1;


-- ============================================================
-- PENDING RESOURCES
-- ============================================================

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

WHERE r.status='Pending'

ORDER BY r.upload_date DESC;


-- ============================================================
-- APPROVE RESOURCE
-- ============================================================

UPDATE resources

SET status='Approved'

WHERE resource_id = 1;


-- ============================================================
-- REJECT RESOURCE
-- ============================================================

UPDATE resources

SET status='Rejected'

WHERE resource_id = 1;


-- ============================================================
-- UPDATE RESOURCE
-- ============================================================

UPDATE resources

SET

    title='Updated Title',

    description='Updated Description',

    file_link='https://example.com',

    subject_id=1,

    type_id=1,

    status='Pending'

WHERE resource_id=1;


-- ============================================================
-- DELETE RESOURCE
-- ============================================================

DELETE FROM resources

WHERE resource_id=1;


-- ============================================================
-- REGISTER NEW USER
-- ============================================================

INSERT INTO users

(
    username,
    email,
    password
)

VALUES

(
    'sampleuser',
    'sample@email.com',
    'hashed_password'
);


-- ============================================================
-- ADD NEW RESOURCE
-- ============================================================

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

(
    'Sample Resource',
    'Description',
    'https://drive.google.com/...',
    1,
    1,
    1
);


-- ============================================================
-- DASHBOARD STATISTICS
-- ============================================================

SELECT

    COUNT(*) AS total,

    SUM(status='Pending') AS pending,

    SUM(status='Approved') AS approved,

    SUM(status='Rejected') AS rejected

FROM resources;


-- ============================================================
-- RESOURCES BY STATUS
-- ============================================================

SELECT

    r.resource_id,

    r.title,

    u.username,

    s.subject_name,

    r.status,

    r.upload_date

FROM resources r

JOIN users u
ON r.user_id = u.user_id

JOIN subjects s
ON r.subject_id = s.subject_id

WHERE r.status='Approved'

ORDER BY r.upload_date DESC;