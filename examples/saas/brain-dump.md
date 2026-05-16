# SaaS for indie therapists

Ok so my sister is a therapist and she keeps complaining that all the
practice-management SaaS out there is bloated, charges $80/mo, and is built
for clinics not solo practitioners. I want to build something dead simple.

She wants to:
- log sessions with clients (super basic notes, encrypted at rest)
- send invoices via Stripe
- schedule appointments (calendar sync — google + apple)
- HIPAA-ish privacy even though we're not pursuing full compliance day 1
- a tiny dashboard showing this-week income + upcoming sessions

Constraints:
- Budget is basically zero. Must run on cheap infra ($20/mo ceiling).
- Solo dev (me, weekends). Deadline: 8 weeks to a private beta with her.
- Must work on phone (she sees clients in cafes sometimes).

Risks:
- Scary thing: HIPAA. If I screw up encryption I am toast.
- Risk: Stripe taking 3% on already-tight margins.
- Worried about: client data export if we shut down.

Open questions:
- Do I really need separate web + mobile, or is PWA enough?
- Should I use Supabase auth or roll my own?
- Is e2e encryption overkill for session notes?

Goal: get her using it daily by end of Q3. Goal: 10 other therapists using it by EOY.
