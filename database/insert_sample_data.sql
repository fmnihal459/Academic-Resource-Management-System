INSERT INTO subjects (subject_code, subject_name) 
VALUES 
-- General Education (GED) Courses
('ENG114', 'English I'),
('ENG115', 'English II'),
('GED119', 'Ethics and Cyber Law'),
('GED129', 'Functional Bangla'),
('GED201', 'Bangladesh Studies'),
('GED202', 'History of Emergence of Bangladesh'),
('GED213', 'Principles of Economics & Entrepreneurship Development'),
('GED215', 'Industrial Management & Financial Accounting'),
('GED219', 'Engineering Economics'),
('GED321', 'Accounting'),
('GED421', 'Industrial Management'),
('GED431', 'Business Communication'),

-- Science & Mathematics Courses
('PHY111', 'Physics I'),
('PHY124', 'Physics II'),
('MAT112', 'Differential & Integral Calculus'),
('MAT123', 'Differential Equation & Laplace Transform'),
('MAT135', 'Matrices, Complex Variable & Fourier Analysis'),
('STA215', 'Basic Statistics & Probability'),
('MAT216', 'Geometry & Vector Analysis'),
('MAT235', 'Numerical Methods'),

-- Core Courses
('CSE121', 'Structured Programming'),
('CSE122', 'Structured Programming Lab'),
('CSE123', 'Basic Electrical Engineering'),
('CSE124', 'Basic Electrical Engineering Lab'),
('CSE125', 'Discrete Mathematics'),
('CSE127', 'Basic Electrical and Electronic Engineering'),
('CSE128', 'Basic Electrical and Electronic Engineering Lab'),
('CSE131', 'Basic Electronics Engineering'),
('CSE132', 'Basic Electronics Engineering Lab'),
('CSE133', 'Data Structure'),
('CSE134', 'Data Structure Lab'),
('CSE200', 'Competitive Programming'),
('CSE211', 'Digital Logic Design'),
('CSE212', 'Digital Logic Design Lab'),
('CSE213', 'Computer Organization & Architecture'),
('CSE215', 'Communication Engineering'),
('CSE221', 'Object Oriented Programming'),
('CSE222', 'Object Oriented Programming Lab'),
('CSE223', 'Database Management System'),
('CSE224', 'Database Management System Lab'),
('CSE231', 'Algorithm'),
('CSE232', 'Algorithm Lab'),
('CSE237', 'Microprocessor & Interfacing'),
('CSE238', 'Microprocessor & Interfacing Lab'),
('CSE300', 'Project'),
('CSE311', 'Computer Networks'),
('CSE312', 'Computer Networks Lab'),
('CSE321', 'Operating System'),
('CSE322', 'Operating System Lab'),
('CSE323', 'Web Programming'),
('CSE327', 'Theory of Computation'),
('CSE415', 'Compiler Construction'),
('CSE416', 'Compiler Construction Lab'),
('CSE417', 'Software Engineering & Design Pattern'),
('CSE418', 'Software Engineering & Design Pattern Lab'),
('CSE421', 'Artificial Intelligence'),
('CSE422', 'Artificial Intelligence Lab'),
('CSE427', 'Introduction to Data Science'),
('CSE428', 'Introduction to Data Science Lab'),
('CSE436', 'Final Year Project'),

-- Optional Courses
('CSE401', 'Computer Graphics & Image Processing'),
('CSE402', 'Computer Graphics & Image Processing Lab'),
('CSE403', 'Embedded System Design'),
('CSE404', 'Embedded System Design Lab'),
('CSE413', 'Optical Communication'),
('CSE414', 'Optical Communication Lab'),
('CSE425', 'Neural Network'),
('CSE426', 'Neural Network Lab'),
('CSE431', 'LSI Design'),
('CSE432', 'VLSI Design Lab'),
('CSE441', 'Digital Signal Processing'),
('CSE442', 'Digital Signal Processing Lab'),
('CSE443', 'Natural Language Processing'),
('CSE444', 'Natural Language Processing Lab'),
('CSE453', 'Cloud Computing'),
('CSE454', 'Cloud Computing Lab'),
('CSE455', 'Contemporary Course on Computer Science'),
('CSE456', 'Contemporary Course Lab on Computer Science'),
('CSE457', 'Parallel Processing'),
('CSE458', 'Parallel Processing Lab'),
('CSE463', 'Advanced Database System'),
('CSE464', 'Advanced Database System Lab'),
('CSE465', 'Digital Image Processing'),
('CSE466', 'Digital Image Processing Lab'),
('CSE469', 'Bioinformatics Computing'),
('CSE470', 'Bioinformatics Computing Lab'),
('CSE471', 'Machine Learning'),
('CSE472', 'Machine Learning Lab');

-- Passwords below are Werkzeug (scrypt) hashes of:
-- admin -> admin123, fardin -> fardin123, rakib -> rakib123,
-- nusrat -> nusrat123, sarah -> sarah123
INSERT INTO users (username, email, password, role)
VALUES
('admin', 'admin@gmail.com', 'scrypt:32768:8:1$83xpccZvkZcgg8bc$8863a112bf42dee9f7b3ab6173781d9768141b93bf739436405002840a8f1ad32fa505c876c48e1df10811998bffcc39941e256f4260df5f3330b3cdc0095405', 'admin'),

('fardin', 'fardin@gmail.com', 'scrypt:32768:8:1$K2DlcJPdubBZq4DJ$0b6b7622b723e4b56f31a60a00ca545afbdc4a98fbcb175ffd4ce8fd37d710bbaa1c6626582c624f9f62fc82e3e2a8eb3579ec6e8105518d513d32809761be89', 'user'),

('rakib', 'rakib@hotmail.com', 'scrypt:32768:8:1$2b4jR0RE48KbzOho$2129549b29962bd09860eea032ed7f3533145e775db13607a38fcf6a64a00abba809b9323ed9f6e9f0273832924b46396b3bbd9964afd257efed105f0b8c6755', 'user'),

('nusrat', 'nusrat@outlook.com', 'scrypt:32768:8:1$gLbLHCBkD4Uq4CkU$751abbac22c0e987e2c283783285b72f8bd4c4106b419d6af135129f097e12ff1dbcd9a5a6007980745a4377da07fbe33c3513572b55e80f81adb0bbb43317ae', 'user'),

('sarah', 'sarah@yahoo.com', 'scrypt:32768:8:1$VkkAtkSo8j3fcSKJ$016900d3afedea0fac9c3f29dbd016ef4abdc9a5f648a19300e5bead2d93f2135e262b42f49af7f490018d94304ed32046275ed756b62fd8c2362f1e0acf9f3e', 'user');

INSERT INTO resource_types (type_name)
VALUES
('Lecture Note'),
('Assignment'),
('Lab Report'),
('Lecture Slide'),
('Previous Question');

INSERT INTO resources
(
title,
description,
file_link,
subject_id,
type_id,
user_id,
status
)

VALUES

(
'DBMS ER Diagram Notes',
'Detailed notes on ER diagrams and normalization.',
'https://drive.google.com/dbms1',
5,
1,
2,
'Approved'
),

(
'OOP Assignment 2',
'Implementation of inheritance and polymorphism.',
'https://drive.google.com/oopassignment',
4,
2,
3,
'Approved'
),

(
'Data Structures Lab Report',
'Linked List implementation report.',
'https://drive.google.com/dslab',
2,
3,
2,
'Approved'
),

(
'Structured Programming Slide',
'Introduction to Structured Programming.',
'https://drive.google.com/agileppt',
1,
4,
4,
'Approved'
),

(
'Statistics Previous Batch Questions',
'Final questions of previous semesters.',
'https://drive.google.com/statmid',
8,
5,
5,
'Approved'
);
