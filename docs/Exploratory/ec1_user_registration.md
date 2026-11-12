# EC-01 — New User Registration

## Mission
Explorer new user registration to identify the validation issue, account creation issue, and unclear registration rules 

## Scope
- Registration form and required fields.
- Username and email handling.
- Password and confirmation.
- Successful account creation.
- Login using the newly created account.
- Direct HTTP request testing in this session.

## Out of Scope
- Teacher approval.
- Course enrollment and payment.
- Load testing.

## Timebox
45 minutes.

## Environment
- Local application: http://127.0.0.1:8000
- Application commit: 496dd4d
- Browser and version: Chrome.
- Tester: Majd Kassem
- Date: Nov,12 2026

## Preconditions
- Application is running.
- Tester is logged out.
- Synthetic registration data is prepared.

## Information Basis
- Product overview.
- Registration form labels and messages.
- Existing assumptions and open questions.

## Session Notes

| ID | Action and Data | Actual Result | Follow-up |
|---|---|---|---|
| N-01 | Submit the registration form with valid data. | An account was created. A redirect to the homepage was reported in the session notes. | Confirm the destination: an earlier captured request showed a redirect to `/login/`. |
| N-02 | Submit an empty registration form through the browser. | Browser validation blocked submission. | This does not establish server-side validation for every required field. |
| N-03 | Explore which fields are required. | Browser validation was observed for the username and password fields. | Record the exact field names and check remaining fields individually. |
| N-04 | Submit a password considered common by the tester. | Registration accepted the password despite displayed guidance against common passwords. | Record the test data and exact guidance. Confirm the intended password policy. |
| N-05 | Register using an existing username. | Registration was rejected with a message reported as clear. | Capture the exact message and confirm no additional account was created. |
| N-06 | Register using a new username and an existing email address. | Registration was rejected with a message reported as clear. | Capture the exact message and confirm no additional account was created. |
| N-07 | Send a registration POST request through Postman with an empty username and valid CSRF protection. | The server rejected registration, and no account was created. | Repeat with other required fields individually. |

## Evidence

The original notes reference `screenshot-01.png` for every observation.
Evidence mapping has not yet been verified.

- Link each observation to the screenshot or response that supports it.
- Record exact error messages and relevant test data.
- Remove passwords, cookies, and tokens from shared evidence.

## Session Summary

### Coverage Achieved

- Valid registration.
- Empty-form browser validation.
- Required-field exploration for username and passwords.
- Common-password acceptance.
- Duplicate username handling.
- Duplicate email handling.
- Server-side rejection of an empty username.

### Findings

- Account creation succeeded with valid input.
- Browser validation blocked empty-form submission.
- Duplicate username and email registration attempts were rejected.
- Server-side validation rejected an empty username.
- Password guidance and observed acceptance may be inconsistent.
- The successful-registration redirect destination needs clarification.

### Open Questions

1. What password policy should registration enforce?
2. Should common passwords be rejected or merely discouraged?
3. Should successful registration redirect to the homepage or login page?

### Not Demonstrated by the Current Notes

- Rejection of mismatched password and confirmation.
- Login using the newly created account.
- Invalid email format handling.
- Server-side validation of required fields other than username.

These items remain unverified unless supporting execution notes
and evidence are added.

### Follow-up Actions

- Confirm the registration redirect destination.
- Complete missing test data and evidence references.
- Investigate password-policy behavior.
- Explore mismatched passwords and login with a new account.
- Check other required fields through direct HTTP requests.
- Update assumptions and risks based on the findings.

## Session Conclusion

The session provides initial registration coverage.
It does not establish that every registration rule works correctly.

The password-policy observation requires further investigation
before being classified as a confirmed defect.