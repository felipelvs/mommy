# Requirements Specification

Here you will find the project's functional and non-functional requirements.
Requirements are essential for understanding what tasks the system must
perform and how they will be performed.

I decided to separate the requirements by "modules" to improve understanding.

## General

### NFR 001

It must run on the World Wide Web.

### NFR 002

It must use these technologies: **HTML**, **CSS**, **JavaScript**, **Python**,
and **Flask**.

### NFR 003

It should use the following tools to keep the project consistent:
**Prettier**, **Black**, **isort**, and **Flake8**.

### NFR 004

All pages must be responsive.

### NFR 005

The system must store the persistent data in a relational database.

### NFR 006

Go off the air in case of inefficiency, returning only when repaired.

## Authentication

**Restriction**: None.

### NFR 007

The system must record/traffic the user's **id** using a random UUID rather
than ascending numbers.

### NFR 008

The system must record/traffic the user's **password** using the bcrypt
encryption algorithm.

### FR 001

The system must allow the user to create an account.

- The form must have the following fields: `email`, `password` and
  `confirm_password`.
- The `email` field must allow a minimum of 6 and a maximum of 254 characters.
- The `password` field must allow a minimum of 8 and a maximum of 38
  characters.
- The `confirm_password` field must allow a minimum of 8 and a maximum of 38
  characters.
- All form fields must be mandatory.
- Fields with invalid data must be highlighted.
- It should display toasts on successful and unsuccessful attempts.
- It must redirect the user to the login page if the attempt is successful.

### FR 002

The system must allow the user to sign into their account.

- The form must have the following fields: `email` and `password`.
- The `email` field must allow a minimum of 6 and a maximum of 254 characters.
- The `password` field must allow a minimum of 8 and a maximum of 38
  characters.
- All form fields must be mandatory.
- Fields with invalid data must be highlighted.
- It should display toasts on unsuccessful attempts.
- It must redirect the user to the **Dashboard** if the attempt is successful.

## Dashboard

**Restriction**: The user must be logged into the system to access the module.

### NFR 009

The system must record/traffic the month's **id** using a random UUID rather
than ascending numbers.

### FR 003

The system should allow the user to add prototypes in the month.

- The form must have the following fields: `name`, `stones`, `made`,
  and `value`.
- The `name` field must allow a minimum of 2 and a maximum of 32 characters.
- The `stones` field must limit the number to a minimum of 1 and a maximum
  of 400.
- The `made` field must limit the number to a minimum of 1 and a maximum
  of 300.
- The `value` field must only accept the values "0.025" and "0.040".
- All form fields must be mandatory.
- It should display toasts on successful and unsuccessful attempts.
- It must redirect the user to the **Dashboard** on successful and
  unsuccessful attempts.

### FR 004

The system should list all prototypes added in the month.

- The data must be: `registration date`, `name`, `stones`, `value`,
  `qty of prototypes`, `qty of stones`, and `profit`.

### FR 005

The system should allow the user to remove prototypes added in the month.

- It must consult the user with a confirmation before removal.
- It should display toasts on successful and unsuccessful attempts.
- It must redirect the user to the **Dashboard** on successful and
  unsuccessful attempts.

### FR 006

The system should display the monthly summary.

- The data must be: `month`, `total prototypes`, `total stones`, and `profit`.

### FR 007

The system should allow the user to close the month.

- It must consult the user with a confirmation before closing.
- New month must be the current month of the server if it is closed from day 1
  to day 5.
- New month must be the following server month if it is closed before day 1
  and after day 5.
- The user cannot be allowed to end the month if the user's month is the
  following month from the server.
- It should display toasts on successful and unsuccessful attempts.
- It must redirect the user to the dashboard on successful and unsuccessful
  attempts.

### FR 008

The system should allow the user to share their months with other people.

- It must copy a link from the share page by clicking the share button.
- The share page must follow the requirements of the **Share** module.

## Share

**Restriction**: None.

### FR 009

The share page should display every month of the user.

- When clicking on a month, a page should open following the requirements
  **RF 004** and **RF 006**.
