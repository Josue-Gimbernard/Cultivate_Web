from __future__ import annotations

import os
from dataclasses import dataclass

from flask import Flask, redirect, render_template, request, session, url_for


@dataclass(frozen=True)
class Space:
    name: str
    audience: str
    role: str
    phase: str
    detail: str
    dependencies: tuple[str, ...]
    feeling: str
    first_version: str
    future_version: str


@dataclass(frozen=True)
class ReadinessItem:
    name: str
    status: str
    summary: str
    next_step: str


@dataclass(frozen=True)
class DayMoment:
    time: str
    title: str
    location: str
    story: str
    owner_note: str


@dataclass(frozen=True)
class VoicePair:
    use: str
    avoid: str
    reason: str


@dataclass(frozen=True)
class OfferBucket:
    name: str
    audience: str
    role: str
    status: str
    includes: tuple[str, ...]
    pricing_note: str


@dataclass(frozen=True)
class DecisionItem:
    decision: str
    recommendation: str
    risk: str
    unlocks: str


@dataclass(frozen=True)
class DecisionRiskSummary:
    risk: str
    count: int
    meaning: str
    meeting_move: str


@dataclass(frozen=True)
class WalkthroughSlide:
    label: str
    title: str
    story: str
    proof: str
    action: str
    speaker_note: str
    route: str


@dataclass(frozen=True)
class JourneyStep:
    phase: str
    title: str
    family_state: str
    cultivate_response: str
    proof_point: str
    owner_question: str


@dataclass(frozen=True)
class RoadmapPhase:
    phase: str
    title: str
    purpose: str
    build_focus: str
    validation_gate: str
    owner_output: str


@dataclass(frozen=True)
class ConcernItem:
    topic: str
    family_question: str
    safe_response: str
    avoid: str
    internal_note: str


@dataclass(frozen=True)
class EvidenceItem:
    source: str
    what_it_supports: str
    site_usage: str
    confidence: str
    owner_check: str


@dataclass(frozen=True)
class PainPoint:
    audience: str
    tension: str
    cultivate_response: str
    boundary: str


@dataclass(frozen=True)
class GlossaryTerm:
    term: str
    plain_meaning: str
    use_on_site: str
    avoid_saying: str


@dataclass(frozen=True)
class ComparisonItem:
    frame: str
    is_text: str
    is_not_text: str
    why_it_matters: str


@dataclass(frozen=True)
class AssumptionItem:
    assumption: str
    safe_basis: str
    current_use: str
    owner_needed: str


@dataclass(frozen=True)
class OwnerInputItem:
    category: str
    question: str
    why_it_matters: str
    answer_shape: str
    unlocks: str
    support_route: str


@dataclass(frozen=True)
class PostMeetingUpdate:
    step: str
    title: str
    update_target: str
    why_it_matters: str
    guardrail: str
    support_route: str


@dataclass(frozen=True)
class OwnerReviewPrepItem:
    step: str
    title: str
    check: str
    why_it_matters: str
    support_route: str


@dataclass(frozen=True)
class OwnerMeetingScriptStep:
    timebox: str
    title: str
    say: str
    show_route: str
    capture: str
    avoid: str


@dataclass(frozen=True)
class OwnerMeetingRecapItem:
    section: str
    purpose: str
    starter_text: str
    next_source: str
    support_route: str


@dataclass(frozen=True)
class OwnerReviewPacketItem:
    phase: str
    title: str
    purpose: str
    output: str
    route: str


@dataclass(frozen=True)
class PublicDraftItem:
    page: str
    purpose: str
    ready_source: str
    hold_until: str
    next_build: str
    route: str


@dataclass(frozen=True)
class ReviewSurface:
    group: str
    title: str
    use_when: str
    owner_question: str
    route: str


@dataclass(frozen=True)
class NavItem:
    label: str
    route: str
    match_routes: tuple[str, ...] = ()


@dataclass(frozen=True)
class NavSection:
    title: str
    items: tuple[NavItem, ...]


@dataclass(frozen=True)
class CommandStep:
    number: str
    title: str
    summary: str
    route: str


@dataclass(frozen=True)
class MeetingTrack:
    label: str
    title: str
    summary: str


@dataclass(frozen=True)
class GuidedReviewStep:
    label: str
    title: str
    summary: str
    route: str


@dataclass(frozen=True)
class DraftNavItem:
    label: str
    route: str
    status: str


@dataclass(frozen=True)
class PublishGateItem:
    label: str
    status: str
    summary: str
    route: str


@dataclass(frozen=True)
class ApprovalItem:
    claim: str
    status: str
    source_basis: str
    public_stance: str
    owner_action: str
    route: str


@dataclass(frozen=True)
class ApprovalSummary:
    status: str
    count: int
    meaning: str
    next_move: str


@dataclass(frozen=True)
class CohortBlock:
    week: str
    theme: str
    teen_focus: str
    middle_focus: str
    parent_focus: str
    evidence: str


@dataclass(frozen=True)
class ImpactSignal:
    signal: str
    why_it_matters: str
    how_to_capture: str
    review_cadence: str
    next_decision: str


@dataclass(frozen=True)
class BriefSection:
    label: str
    title: str
    summary: str
    support: str


@dataclass(frozen=True)
class NextAction:
    lane: str
    action: str
    why_now: str
    output: str
    support_route: str


@dataclass(frozen=True)
class ActionLaneSummary:
    lane: str
    count: int
    purpose: str
    next_move: str


SPACES = [
    Space(
        "The Sprout Space",
        "Ages 0-5",
        "On-site childcare vision",
        "Validate",
        "Warm, play-based care that lets families participate without arranging separate childcare.",
        ("DCF licensing", "background checks", "staff ratios", "teen helper boundaries"),
        "Calm, secure, sensory-rich, and close enough for parents to breathe.",
        "Discovery-only until childcare licensing is validated.",
        "Licensed on-site childcare with trained adult staff and carefully bounded teen helper pathways.",
    ),
    Space(
        "The Stepping Stones",
        "Ages 6-12",
        "Middle-kid making and discovery",
        "Cohort",
        "Hands-on projects, early life skills, creative exploration, and a bridge toward The Summit.",
        ("project supplies", "facilitators", "outdoor access", "bridge moments"),
        "Warm structure with enough freedom for curiosity to become confidence.",
        "Hands-on project blocks for a small founding cohort.",
        "A full middle-kids community space with bridge programming and outdoor/garden connections.",
    ),
    Space(
        "The Summit",
        "Ages 13-18",
        "Teen life skills and belonging",
        "Cohort",
        "Judgment-free teen community built around real skills, communal rhythm, and meaningful responsibility.",
        ("life-skills workshops", "inclusive staff", "mentorship", "project space"),
        "Unhurried, grounded, and genuinely theirs.",
        "The anchor program for teens in the founding cohort.",
        "A mature teen community with cafe, childcare, garden, media, mentorship, and project pathways.",
    ),
    Space(
        "The Harvest Cafe",
        "Campus",
        "Teen-run cafe vision",
        "Validate",
        "A future community cafe where teens learn hospitality, food costs, service, and small-business thinking.",
        ("food-service path", "kitchen", "teen work rules", "possible coffee partner"),
        "Warm, bustling, handmade, and connected to everything else.",
        "Communal snack/lunch rhythm only; no public cafe promise.",
        "Teen-run cafe with food-service compliance, catering, and possible coffee partner.",
    ),
    Space(
        "The Grove",
        "Parents",
        "Work lounge and community",
        "Cohort",
        "A calm parent landing place that turns waiting time into work, friendship, and community contribution.",
        ("wifi", "work tables", "parent rhythm", "community hosting"),
        "Like a beloved neighborhood coffee shop with better purpose.",
        "Parent lounge/work tables during cohort sessions.",
        "Full co-working lounge with desk options, call pods, and day/monthly access.",
    ),
    Space(
        "The Commons",
        "Community",
        "Workshops and shared gatherings",
        "Cohort",
        "A flexible room for workshops, family gatherings, co-op energy, and eventually community rentals.",
        ("room setup", "guidelines", "insurance", "booking rules"),
        "Flexible, welcoming, useful, and easy to reconfigure.",
        "Shared workshop and showcase room for the cohort.",
        "Rentable community space for co-ops, workshops, events, and gatherings.",
    ),
    Space(
        "The Wilds",
        "All ages",
        "Outdoor campus vision",
        "Validate",
        "The outdoor campus: Sprout Yard, Range, Canopy, Growing Grounds, and Garden Guild.",
        ("site", "safety", "accessibility", "supervision", "maintenance"),
        "Open air, movement, restoration, stewardship, and a little wonder.",
        "Light outdoor rhythm or container garden if the site allows.",
        "Full outdoor campus with Sprout Yard, Range, Canopy, Growing Grounds, and Garden Guild.",
    ),
]

READINESS = [
    ReadinessItem(
        "Vision and brand",
        "Ready to show",
        "The owner-updated docs give the site a clear emotional center and visual language.",
        "Use the preview to align on tone, names, and story.",
    ),
    ReadinessItem(
        "Founding cohort",
        "Ready to shape",
        "The first safe launch can center teens, middle kids, parents, and a simple five-week rhythm.",
        "Choose the public label, target size, and days/times.",
    ),
    ReadinessItem(
        "Childcare",
        "Validate first",
        "The Sprout Space is powerful but licensing, ratios, staff credentials, and teen boundaries are unresolved.",
        "Call the relevant Florida/county licensing path before promising care.",
    ),
    ReadinessItem(
        "Cafe and Foxtail",
        "Validate first",
        "The Harvest Cafe and Foxtail idea should stay aspirational until food-service and partner terms are real.",
        "Validate food-service path and decide if/when to approach Foxtail.",
    ),
    ReadinessItem(
        "Paid teen roles",
        "Validate first",
        "Teen work is central to the concept, but paid roles need employment, insurance, and supervision boundaries.",
        "Write allowed/prohibited teen tasks by age before offering roles.",
    ),
    ReadinessItem(
        "Outdoor campus",
        "Future build",
        "The Wilds adds richness, but site, safety, accessibility, and maintenance need validation.",
        "Prototype garden or outdoor rhythm lightly before playground buildout.",
    ),
]

DAY_MOMENTS = [
    DayMoment(
        "8:45",
        "Families arrive without the rush.",
        "Village entry",
        "A parent walks in with a teen, a middle kid, and a laptop bag. The day starts with welcome, not a bell. Kids know where they are headed, and parents are not left hovering in a hallway.",
        "For the first cohort, this can be tested with a simple check-in table and clear family flow.",
    ),
    DayMoment(
        "9:15",
        "The Summit settles in.",
        "The Summit",
        "Teens drift into the room, find their people, and ease into the day. The feeling is intentionally unhurried: safe, grounded, and not performative.",
        "Use this as emotional proof of concept before promising formal teen employment pathways.",
    ),
    DayMoment(
        "9:30",
        "Middle kids start making.",
        "The Stepping Stones",
        "The Stepping Stones begins with a warm gathering and a real project. Kids build, test, ask questions, and practice the kind of responsibility that feels like adventure.",
        "This is one of the safest first-cohort anchors because it is programmatic, not heavily regulated childcare.",
    ),
    DayMoment(
        "10:00",
        "Parents have somewhere to land.",
        "The Grove",
        "A few parents open laptops. Someone takes a quiet call. Another parent offers to lead a workshop next week. The parent space makes community possible because adults have a reason to stay.",
        "The Grove can start as a practical lounge before becoming a full co-working product.",
    ),
    DayMoment(
        "11:00",
        "Food becomes a rhythm.",
        "Commons / kitchen table",
        "The campus energy shifts toward food, conversation, and care. Teens think through hospitality and meal planning. Kids see food as a shared responsibility, not just a break.",
        "For early launch, frame this as communal rhythm or snack/lunch planning, not a public cafe.",
    ),
    DayMoment(
        "1:00",
        "Projects cross ages.",
        "Shared workshop space",
        "A teen helps a younger kid solve a build problem. A parent shares a practical skill. The room starts to feel like a village because every person has something to offer.",
        "This is the heart of the founding cohort: cross-age contribution without overpromising regulated services.",
    ),
    DayMoment(
        "2:30",
        "The day ends with evidence.",
        "Village Wall",
        "Before families leave, the work becomes visible: a photo, a quote, a project note, a small win. The Village Wall turns progress into belonging.",
        "Low-cost, high-emotion, and perfect for owner preview and first cohort.",
    ),
]

VOICE_PAIRS = [
    VoicePair(
        "A homeschool family campus in Central Florida.",
        "A school, daycare, cafe, and coworking center all in one.",
        "The first phrase is clear and flexible. The second creates regulated or overbuilt expectations.",
    ),
    VoicePair(
        "A place where real-life skills become part of the week.",
        "Guaranteed life-skills outcomes for every child.",
        "Keep the promise experiential, not outcome-guaranteed.",
    ),
    VoicePair(
        "A future cafe vision centered on teen learning.",
        "A teen-run cafe opening soon.",
        "Food service and teen work need validation before public claims.",
    ),
    VoicePair(
        "A founding cohort helping shape what Cultivate becomes.",
        "Enrollment is open for the full campus.",
        "The first launch is still a careful owner/founder decision.",
    ),
    VoicePair(
        "Designed with neurodiverse families in mind.",
        "Therapeutic services for neurodiverse children.",
        "Inclusion is central, but therapy/service claims need specific credentials and approvals.",
    ),
]

OFFER_BUCKETS = [
    OfferBucket(
        "Family Membership",
        "Whole family",
        "Base relationship with Cultivate",
        "Model next",
        ("community access", "founding family updates", "week-five events", "eligibility for program add-ons"),
        "No price set. Model against facility, staffing, and cohort size.",
    ),
    OfferBucket(
        "The Summit",
        "Ages 13-18",
        "Teen life-skills and community program",
        "Cohort anchor",
        ("life-skills workshops", "projects", "creative/media work", "communal rhythm", "mentorship pathways"),
        "Likely core program pricing, but must reflect staffing and schedule.",
    ),
    OfferBucket(
        "The Stepping Stones",
        "Ages 6-12",
        "Middle-kid making and discovery",
        "Cohort anchor",
        ("hands-on projects", "early life skills", "creative exploration", "bridge moments"),
        "Could be priced as program add-on or cohort seat.",
    ),
    OfferBucket(
        "The Grove",
        "Parents",
        "Parent workspace and community",
        "Light first version",
        ("work tables", "wifi", "parent community", "skill-sharing", "future day/monthly options"),
        "Do not price as full co-working until amenities are known.",
    ),
    OfferBucket(
        "The Commons",
        "Members/community",
        "Workshops, gatherings, and future rentals",
        "Internal first",
        ("cohort workshops", "showcases", "family gatherings", "future rentals"),
        "Public rental pricing requires facility, insurance, and booking rules.",
    ),
    OfferBucket(
        "Community Fund",
        "Optional supporters",
        "Accessibility and program support",
        "Design carefully",
        ("voluntary donations", "supply support", "future subsidy support", "Village Wall recognition"),
        "Needs accounting, governance, and scholarship rules before public claims.",
    ),
]

DECISIONS = [
    DecisionItem(
        "First launch shape",
        "Limited founding cohort",
        "Medium",
        "Lets Cultivate test demand and rhythm before committing to the full campus.",
    ),
    DecisionItem(
        "Teen space name",
        "Use The Summit publicly; preserve The Glade as source provenance",
        "Low",
        "Clarifies the family journey from Sprout to Stones to Summit to world ready.",
    ),
    DecisionItem(
        "Ages in first cohort",
        "Anchor on teens and middle kids; keep 0-5 discovery-only",
        "Medium",
        "Avoids childcare promises until licensing and staffing are validated.",
    ),
    DecisionItem(
        "Cafe stance",
        "Treat Harvest Cafe as future vision during first cohort",
        "High",
        "Keeps food-service and teen employment questions from blocking the first test.",
    ),
    DecisionItem(
        "Foxtail timing",
        "Approach after facility and cafe path are clearer",
        "Medium",
        "Protects the partnership conversation from premature operational assumptions.",
    ),
    DecisionItem(
        "Interest page",
        "Keep disabled/private until intake process is approved",
        "Low",
        "Allows owner review now without collecting real family data yet.",
    ),
]


DECISION_RISK_GUIDE = (
    (
        "Low",
        "Naming or review-flow decisions that can usually be approved quickly.",
        "Confirm, revise wording, or mark as held.",
    ),
    (
        "Medium",
        "Shape decisions that affect public copy, first-cohort scope, or sequencing.",
        "Choose a lane before drafting public language.",
    ),
    (
        "High",
        "Operational decisions that could imply regulated services, food service, employment, or partnerships.",
        "Keep private and validation-first until the path is clear.",
    ),
)


def build_decision_risk_summaries(
    decisions: tuple[DecisionItem, ...] | list[DecisionItem],
) -> tuple[DecisionRiskSummary, ...]:
    counts = {risk: 0 for risk, _meaning, _meeting_move in DECISION_RISK_GUIDE}
    for decision in decisions:
        counts[decision.risk] = counts.get(decision.risk, 0) + 1
    return tuple(
        DecisionRiskSummary(risk, counts.get(risk, 0), meaning, meeting_move)
        for risk, meaning, meeting_move in DECISION_RISK_GUIDE
        if counts.get(risk, 0)
    )


WALKTHROUGH_SLIDES = [
    WalkthroughSlide(
        "01 / Opening",
        "Cultivate is a village for the whole homeschool family.",
        "The owner should feel the complete ecosystem first: kids, teens, parents, work, food, outdoor rhythm, and community all supporting one another.",
        "The strongest source-doc language is not about a single program. It is about a family campus where real skills become part of ordinary life.",
        "Start with the full emotional picture, then quickly show the safer first launch lane.",
        "Set the frame: this is the owner's private concept room, not public copy yet.",
        "owner_preview",
    ),
    WalkthroughSlide(
        "02 / First move",
        "Launch the rhythm before launching the full campus.",
        "The founding cohort gives Cultivate a credible first version without forcing childcare, cafe, partner, employment, or facility promises too early.",
        "The current recommendation is a limited term anchored by The Summit, The Stepping Stones, The Grove, and The Commons.",
        "Ask for approval on cohort label, audience, term length, and whether the interest page can move from draft to real intake.",
        "Keep this crisp: the first launch is a proof of rhythm, not a smaller dream.",
        "founding_cohort",
    ),
    WalkthroughSlide(
        "03 / Experience",
        "Make the day feel calm, useful, and alive.",
        "The site needs to help the owner imagine families arriving, kids settling, teens contributing, parents breathing, and the day ending with visible evidence of growth.",
        "The day-in-the-life page turns the abstract ecosystem into a lived rhythm without promising a final operating schedule.",
        "Use the story to check whether the experience feels like Cultivate before polishing public copy.",
        "Watch for the owner's face here. If the day feels right, the rest gets easier.",
        "day_at_cultivate",
    ),
    WalkthroughSlide(
        "04 / Campus",
        "Every space has a job, and every job has a launch stance.",
        "The named spaces are a strength, but they need careful boundaries: some are cohort-ready, some are discovery work, and some belong to the longer-range campus.",
        "The space panels separate first version from future version so the full vision stays inspiring without becoming accidental day-one scope.",
        "Confirm which spaces should appear in owner-facing preview, family-facing preview, and internal planning only.",
        "Name the risk kindly: beautiful spaces can accidentally sound like promises.",
        "spaces",
    ),
    WalkthroughSlide(
        "05 / Voice",
        "The brand should feel warm, practical, inclusive, and careful.",
        "Cultivate can sound big-hearted without sounding vague, clinical, or overpromised. The safest copy names the experience and avoids regulated claims.",
        "The Brand Voice Lab gives usable phrase pairs so future pages can stay consistent as the repo grows.",
        "Use this as the copy filter before anything leaves private preview.",
        "This is the guardrail that keeps warmth from turning into overclaiming.",
        "brand_voice",
    ),
    WalkthroughSlide(
        "06 / Decisions",
        "The next meeting should end with shape, not a pile of maybes.",
        "A strong owner walkthrough should turn excitement into clear decisions: launch shape, naming, age scope, cafe stance, partnership timing, and interest page readiness.",
        "The Owner Decision Dashboard frames each choice by recommendation, risk, and what it unlocks.",
        "Close by selecting what gets approved, what stays internal, and what needs validation next.",
        "End with a short approval list. The win is clarity, not solving every future phase.",
        "owner_decisions",
    ),
]


JOURNEY_STEPS = [
    JourneyStep(
        "Discover",
        "A family hears about a different kind of homeschool support.",
        "They are curious, stretched, and trying to picture whether Cultivate is warm, serious, and safe enough to explore.",
        "The preview should lead with the full village idea while staying clear that this is a private planning surface.",
        "Owner preview, ecosystem map, and brand voice.",
        "What should a new family understand in the first sixty seconds?",
    ),
    JourneyStep(
        "Imagine",
        "They need to see themselves in the rhythm.",
        "The parent wonders where they would work, where each child would go, and whether the day would feel calmer than their current week.",
        "A day-in-the-life story makes arrival, projects, parent landing, shared food rhythm, and visible progress easy to picture.",
        "A Day at Cultivate and space detail panels.",
        "Which parts of the day are essential to the first cohort, and which are future atmosphere?",
    ),
    JourneyStep(
        "Trust",
        "They look for boundaries before they share interest.",
        "The family wants confidence that Cultivate knows what is ready now and what still needs licensing, staffing, facility, or partner validation.",
        "Readiness language should make the concept feel more credible, not smaller.",
        "Launch readiness, owner decisions, and guarded interest page.",
        "Which validation items need owner approval before families see public copy?",
    ),
    JourneyStep(
        "Join",
        "They consider a founding family role.",
        "They are not buying a finished campus. They are considering whether they want to help shape a careful first version.",
        "The first offer should feel clear, limited, and useful without inventing prices, dates, or enrollment claims.",
        "Founding cohort and membership model.",
        "What is the exact promise of the first term?",
    ),
    JourneyStep(
        "Belong",
        "The family starts to feel known.",
        "Kids find their spaces, parents find breathing room, and the community starts creating shared evidence of growth.",
        "The site should show belonging as an operating rhythm: projects, contribution, reflection, and the Village Wall.",
        "Walkthrough, day rhythm, and first cohort story.",
        "What visible evidence should families take away each week?",
    ),
    JourneyStep(
        "Grow",
        "The first cohort teaches Cultivate what to build next.",
        "The owner can decide what moves from vision to validated plan: childcare, cafe, teen work, rentals, outdoor campus, and partnership conversations.",
        "The roadmap should turn excitement into sequenced decisions instead of sprawling scope.",
        "Owner decision dashboard and launch readiness.",
        "Which validated signal unlocks the next stage?",
    ),
]


ROADMAP_PHASES = [
    RoadmapPhase(
        "Now",
        "Private owner review",
        "Use the website as a polished concept room for alignment, not as public launch copy.",
        "Owner walkthrough, family journey, decisions, readiness, and source-safe language.",
        "Owner confirms what feels true, what needs changing, and what should remain internal.",
        "Approved direction for first public-facing draft pages.",
    ),
    RoadmapPhase(
        "Next",
        "Validation sprint",
        "Turn the exciting parts into a practical checklist before families see real intake.",
        "Childcare path, cafe stance, teen role boundaries, facility assumptions, and interest workflow.",
        "Unresolved regulated or operational items are named clearly and assigned next steps.",
        "Validation notes and a go/no-go list for the founding family interest page.",
    ),
    RoadmapPhase(
        "First public draft",
        "Founding family interest",
        "Create a careful public-safe expression of the first cohort without opening enrollment prematurely.",
        "Home, about, founding cohort, FAQ, and interest page language.",
        "Privacy language, intake process, contact owner, and approved offer scope are ready.",
        "Public draft pages that can be reviewed before deployment.",
    ),
    RoadmapPhase(
        "First term",
        "Founding cohort",
        "Test rhythm, demand, belonging, and operational load with a limited group.",
        "The Summit, The Stepping Stones, The Grove, The Commons, reflection, and Village Wall evidence.",
        "The first term produces enough feedback to decide what to repeat, pause, or expand.",
        "Cohort recap, family feedback themes, and next-build recommendations.",
    ),
    RoadmapPhase(
        "After proof",
        "Expansion decisions",
        "Move only validated pieces toward fuller operations and keep the vision sequenced.",
        "Childcare, cafe, outdoor campus, rentals, partnership conversations, and membership model.",
        "The owner has evidence, constraints, and capacity to choose the next responsible build.",
        "Phase-two roadmap with approved public claims.",
    ),
]


CONCERN_ITEMS = [
    ConcernItem(
        "What is Cultivate?",
        "Is this a school, daycare, co-op, or coworking space?",
        "Cultivate is being shaped as a homeschool family campus: a community-centered place for real-life skills, parent connection, and age-aware programming.",
        "Calling it a school, licensed daycare, full coworking center, or public cafe before those details are approved.",
        "Keep the category flexible until operating model, licensing, and facility scope are finalized.",
    ),
    ConcernItem(
        "Childcare",
        "Will there be care for younger children?",
        "The Sprout Space is part of the longer-range vision. Before it is offered, the team needs to validate licensing, staffing, ratios, and safety requirements.",
        "Promising childcare, drop-off care, preschool, or teen-led care.",
        "This is one of the highest-risk public claims and should stay validation-first.",
    ),
    ConcernItem(
        "Cafe",
        "Can families buy food or coffee there?",
        "The Harvest Cafe is a future learning vision centered on hospitality and teen skill-building. Early versions should be framed as community rhythm unless food-service details are approved.",
        "Saying a teen-run cafe or Foxtail partnership is opening.",
        "Food service and partner language should wait for owner approval and operational validation.",
    ),
    ConcernItem(
        "Teen work",
        "Will teens have paid jobs?",
        "Cultivate wants teens to practice meaningful responsibility. Any paid role would need clear supervision, age boundaries, task rules, and employment guidance.",
        "Advertising paid teen jobs or implying teens will supervise children.",
        "Keep teen contribution language focused on learning, mentorship, and bounded responsibility.",
    ),
    ConcernItem(
        "Pricing",
        "How much will it cost?",
        "Pricing is not ready for publication. The first step is defining the approved offer, schedule, staffing, facility needs, and founding cohort size.",
        "Publishing placeholder prices or comparing against school, daycare, or coworking pricing.",
        "The membership model page can stay internal until the owner approves real assumptions.",
    ),
    ConcernItem(
        "Timeline",
        "When does this open?",
        "Cultivate is in private planning and owner review. A public timeline should come after the first offer, validation steps, and intake process are approved.",
        "Using opening soon, enrollment open, or exact dates before approval.",
        "The roadmap can show sequence without becoming a launch calendar.",
    ),
]


EVIDENCE_ITEMS = [
    EvidenceItem(
        "09_Cultivate_Full_Ecosystem_FINAL.docx",
        "Owner-updated ecosystem framing and the current whole-campus concept.",
        "Primary source for the private owner preview, roadmap, journey, and overall story.",
        "High",
        "Confirm that this remains the leading source over earlier full-ecosystem files.",
    ),
    EvidenceItem(
        "10_The_Wilds_Outdoor_Campus.docx",
        "Outdoor campus vision: Sprout Yard, Range, Canopy, Growing Grounds, and Garden Guild.",
        "Supports The Wilds as future-build vision and keeps outdoor claims validation-first.",
        "High",
        "Confirm which outdoor elements belong in first-public copy versus future vision.",
    ),
    EvidenceItem(
        "02_The_Sprout_Space.docx",
        "Early-childhood space vision and family support need.",
        "Used carefully as validation-first childcare language, not as a public care offer.",
        "Medium",
        "Validate licensing, staffing, ratios, and teen-helper boundaries before public claims.",
    ),
    EvidenceItem(
        "08_The_Stepping_Stones.docx",
        "Middle-kid bridge programming, hands-on projects, and confidence-building.",
        "Supports the founding cohort recommendation for ages 6-12 project blocks.",
        "High",
        "Confirm age range, session rhythm, and first-term activities.",
    ),
    EvidenceItem(
        "01_The_Glade.docx",
        "Original teen-space concept and belonging-oriented tone.",
        "Preserved as provenance while the site currently uses The Summit as updated naming.",
        "Medium",
        "Confirm final public name for the teen space.",
    ),
    EvidenceItem(
        "05_The_Harvest_Cafe.docx and 06_Foxtail_Partnership.docx",
        "Cafe, hospitality learning, and possible coffee partnership ideas.",
        "Supports future-vision language only; no public cafe or partner promise.",
        "Medium",
        "Confirm when food-service and partnership conversations become real next steps.",
    ),
]


PAIN_POINTS = [
    PainPoint(
        "Parents",
        "Homeschool parents often need community, nearby work time, and a sense that they are not carrying the whole rhythm alone.",
        "The Grove and parent-facing rhythm frame Cultivate as a place for connection, contribution, and breathing room.",
        "Do not promise coworking availability, childcare coverage, or public membership benefits until the owner approves the operating model.",
    ),
    PainPoint(
        "Teens",
        "Teens need belonging, useful responsibility, and a reason to practice real-life skills with people who see them.",
        "The Summit frames teen growth around contribution, mentorship, creativity, hospitality, and readiness for life beyond the home.",
        "Do not imply paid jobs, employment, unsupervised responsibility, or childcare supervision.",
    ),
    PainPoint(
        "Middle kids",
        "Ages 6-12 need a bridge between play and responsibility: projects, confidence, curiosity, and visible progress.",
        "The Stepping Stones gives the first cohort a safe hands-on project lane without depending on the full campus.",
        "Do not turn the project rhythm into a school, graded curriculum, or fixed public schedule without owner approval.",
    ),
    PainPoint(
        "Young children",
        "Younger siblings affect whether families can participate, but early-childhood care carries licensing and staffing realities.",
        "The Sprout Space stays visible as a future family-support vision while the first cohort avoids childcare promises.",
        "Do not advertise childcare, drop-off care, preschool, or teen-helper care until validated.",
    ),
    PainPoint(
        "The owner",
        "The full vision is strong, but it could become too broad if public language promises every space at once.",
        "The site recommends a limited founding cohort first, then evidence-led expansion decisions.",
        "Do not publish launch dates, prices, capacity, partnerships, rentals, cafe operations, or full-campus availability.",
    ),
]


GLOSSARY_TERMS = [
    GlossaryTerm(
        "Cultivate",
        "A private working concept for a homeschool family campus in Central Florida.",
        "Use as the parent brand for the whole ecosystem.",
        "Do not define it as a school, daycare, coworking center, cafe, or public venue until approved.",
    ),
    GlossaryTerm(
        "Founding cohort",
        "A limited first version used to test rhythm, demand, trust, and operational fit before the full campus.",
        "Use as the safest first-launch recommendation.",
        "Do not imply enrollment is open, dates are set, or the offer is approved.",
    ),
    GlossaryTerm(
        "The Summit",
        "Current working name for the teen space and teen growth lane.",
        "Use as the current site name while preserving The Glade as provenance.",
        "Do not treat the name as final public language until the owner confirms it.",
    ),
    GlossaryTerm(
        "The Stepping Stones",
        "Hands-on project and confidence-building lane for middle kids.",
        "Use as a first-cohort-ready concept when paired with approved scope.",
        "Do not define exact ages, schedule, curriculum, or outcomes without owner approval.",
    ),
    GlossaryTerm(
        "The Grove",
        "Parent landing place for work, connection, contribution, and community rhythm.",
        "Use as parent-support language in private preview and careful public drafts.",
        "Do not promise coworking, childcare coverage, or membership access rules yet.",
    ),
    GlossaryTerm(
        "The Commons",
        "Flexible workshop and gathering space concept.",
        "Use as a shared rhythm and workshop frame for the first version.",
        "Do not publish rental, event, or capacity claims yet.",
    ),
    GlossaryTerm(
        "The Sprout Space",
        "Future early-childhood support vision.",
        "Use only as validation-first future vision.",
        "Do not publish as available childcare, preschool, or drop-off care.",
    ),
    GlossaryTerm(
        "The Harvest Cafe",
        "Future hospitality and food-service learning vision.",
        "Use only as future vision unless operations are approved.",
        "Do not publish cafe opening, food sales, teen-run operation, or Foxtail partnership claims.",
    ),
    GlossaryTerm(
        "The Wilds",
        "Future outdoor campus vision.",
        "Use as north-star atmosphere and validation path.",
        "Do not present outdoor campus elements as day-one facilities.",
    ),
]


COMPARISON_ITEMS = [
    ComparisonItem(
        "Category",
        "A developing homeschool family campus concept.",
        "A licensed school, daycare, coworking chain, public cafe, or event venue.",
        "This keeps the public category warm but careful until the operating model is approved.",
    ),
    ComparisonItem(
        "First launch",
        "A limited founding cohort is the safest recommended first step.",
        "A full campus launch with every space operating at once.",
        "The first version should validate culture, demand, and logistics before adding regulated pieces.",
    ),
    ComparisonItem(
        "Teen contribution",
        "A learning path for responsibility, mentorship, hospitality, creativity, and contribution.",
        "A public promise of paid jobs, employment, or teen supervision of children.",
        "Teen language needs to stay clearly educational and supervised.",
    ),
    ComparisonItem(
        "Parent support",
        "A community rhythm that may include parent workspace, connection, and contribution.",
        "A guaranteed coworking membership, childcare substitute, or drop-off solution.",
        "Parent relief matters, but public copy must not overstate the available service.",
    ),
    ComparisonItem(
        "Future spaces",
        "A visible long-range ecosystem that can be validated in sequence.",
        "A promise of childcare, cafe, outdoor campus, rentals, partnerships, or full-campus availability now.",
        "The full vision can inspire without becoming a public commitment.",
    ),
]


ASSUMPTION_ITEMS = [
    AssumptionItem(
        "Cultivate can be framed as a homeschool family campus.",
        "Owner-updated ecosystem docs describe a whole-family community around real-life skills and belonging.",
        "Used as the private preview category and draft public direction.",
        "Owner must approve final public category wording.",
    ),
    AssumptionItem(
        "A limited founding cohort is the responsible first move.",
        "Roadmap, readiness, approval, and operations pages all point toward proving rhythm before full-campus promises.",
        "Used across owner brief, next actions, draft homepage, and cohort draft.",
        "Owner must approve first-cohort label, audience, schedule assumptions, and intake path.",
    ),
    AssumptionItem(
        "The Summit is the current teen-space name.",
        "Updated naming direction is reflected in current web memory while The Glade is preserved as earlier-source provenance.",
        "Used on preview pages as the current teen-space label.",
        "Owner must confirm final public name.",
    ),
    AssumptionItem(
        "The Sprout Space, Harvest Cafe, Foxtail, paid teen work, rentals, and The Wilds remain validation-first.",
        "Source docs support the vision, while approval and readiness pages identify operational and regulatory dependencies.",
        "Used as future-vision or internal planning language only.",
        "Owner must approve when, whether, and how each item can become public copy.",
    ),
    AssumptionItem(
        "Public pages can be drafted privately before they are approved.",
        "The site is gated, has noindex metadata, and marks draft pages as private/unapproved.",
        "Used to build owner-review artifacts without launching claims.",
        "Owner must approve publishing gate items before public release.",
    ),
]


OWNER_INPUT_ITEMS = [
    OwnerInputItem(
        "Story and category",
        "What is the founder origin story we are allowed to tell publicly?",
        "The current site can explain the need, but only the owner can supply the personal why, timeline, and emotional details.",
        "A short founder story, approved words to use, and anything that should stay private.",
        "Public About copy, homepage credibility, and owner bio language.",
        "draft_about",
    ),
    OwnerInputItem(
        "Story and category",
        "What should Cultivate call itself in public copy?",
        "The safest working phrase is homeschool family campus, but the final public category needs owner approval.",
        "One preferred category line plus two words or labels to avoid.",
        "Homepage headline support, FAQ language, and publish-ready navigation.",
        "what_cultivate_is",
    ),
    OwnerInputItem(
        "First cohort",
        "Who is the first cohort actually for?",
        "Age scope determines claims, parent expectations, staffing assumptions, and which spaces can be described as day-one.",
        "Approved age range, parent participation expectations, and whether siblings are included, excluded, or future vision.",
        "Founding cohort page, FAQ answers, and first interest form language.",
        "founding_cohort",
    ),
    OwnerInputItem(
        "First cohort",
        "What schedule, term length, location, and capacity are realistic for the first version?",
        "The site can stay phase-based now, but public copy needs concrete boundaries before families respond.",
        "Preferred days/times, approximate term length, location stance, and target family or child capacity.",
        "Draft cohort details, launch roadmap, and owner-ready intake questions.",
        "cohort_blueprint",
    ),
    OwnerInputItem(
        "Offer and pricing",
        "What can be said about price, membership, donations, and scholarship support?",
        "Pricing language affects trust immediately and should not be guessed from the concept docs.",
        "Approved stance: no pricing yet, estimated range, founder price, application-first, or another model.",
        "Offer model, homepage calls to action, and public FAQ.",
        "membership_model",
    ),
    OwnerInputItem(
        "Operations",
        "Which spaces are actually available in the first version?",
        "Cultivate has a rich campus vision, but day-one availability must stay narrower than the dream unless confirmed.",
        "A list of spaces that are available now, future-only, partner-dependent, or intentionally not public.",
        "Spaces page, homepage proof points, and approval matrix updates.",
        "spaces",
    ),
    OwnerInputItem(
        "Operations",
        "How should Sprout Space, childcare, cafe, Foxtail, rentals, and The Wilds be handled publicly?",
        "These are the highest-risk promise areas because they imply licensing, food service, partnerships, employment, or facilities.",
        "For each item: public now, private vision, validate later, or remove from public copy.",
        "FAQ, source evidence, launch readiness, and public page safety.",
        "launch_readiness",
    ),
    OwnerInputItem(
        "Teen contribution",
        "What kinds of teen responsibility are approved for public description?",
        "The teen vision is compelling, but language must avoid accidental employment or childcare-supervision claims.",
        "Approved examples of teen contribution, supervision boundaries, and words to avoid.",
        "The Summit copy, FAQ responses, and parent trust language.",
        "glossary",
    ),
    OwnerInputItem(
        "Intake and privacy",
        "What information can an interest form collect, and who receives it?",
        "The current interest page is disabled because real family data needs a clear process before collection.",
        "Fields to collect, where responses go, follow-up owner, data-retention stance, and privacy wording.",
        "Enabled interest page, CTA copy, and publish gate clearance.",
        "founding_family_interest",
    ),
    OwnerInputItem(
        "Trust and proof",
        "What photos, testimonials, credentials, partners, or local proof can be used?",
        "The site can be polished without proof, but owner-approved trust assets will make the private preview feel closer to public-ready.",
        "Approved assets, captions, attribution rules, and items that need permission first.",
        "Homepage richness, About credibility, and owner presentation polish.",
        "source_evidence",
    ),
    OwnerInputItem(
        "Public launch",
        "What call to action should a first public page use?",
        "Public visitors need a clear next step, but the CTA must match the approved intake and launch readiness.",
        "Preferred CTA label, destination, contact method, and whether the page is invite-only, interest-only, or application-based.",
        "Draft homepage, cohort page, FAQ, and Railway test-domain review.",
        "public_draft_hub",
    ),
]


POST_MEETING_UPDATES = [
    PostMeetingUpdate(
        "01",
        "Log the owner answer first.",
        "memory/08-owner-answer-log.md",
        "This keeps the durable source of truth in markdown before the site changes.",
        "Do not update public drafts from memory or chat notes alone.",
        "owner_answer_log",
    ),
    PostMeetingUpdate(
        "02",
        "Translate the answer into approval status.",
        "APPROVAL_ITEMS in app.py and /approval-matrix",
        "Each approved, held, or validation-needed answer needs a visible publishing gate.",
        "Only mark a claim ready when the owner answer is specific enough to publish safely.",
        "approval_matrix",
    ),
    PostMeetingUpdate(
        "03",
        "Update assumptions and risk boundaries.",
        "ASSUMPTION_ITEMS in app.py and /assumptions-review",
        "Owner answers either retire assumptions, confirm them, or turn them into validation work.",
        "If an answer is partial, keep the assumption visible instead of smoothing it over.",
        "assumptions_review",
    ),
    PostMeetingUpdate(
        "04",
        "Revise the relevant private draft.",
        "Draft pages, FAQ, offer model, and interest page",
        "Approved answers should make the private public-site packet sharper and less caveated.",
        "Keep draft pages gated until pricing, intake, launch, and operations are cleared.",
        "public_draft_hub",
    ),
    PostMeetingUpdate(
        "05",
        "Update the next-actions queue.",
        "NEXT_ACTIONS in app.py and /next-actions",
        "Every answer should produce either a completed item, a validation task, or a new build step.",
        "Do not leave answered owner questions floating without a next artifact.",
        "next_actions",
    ),
    PostMeetingUpdate(
        "06",
        "Run tests and document the change.",
        "tests/test_routes.py and memory/*.md",
        "The repo should continue to explain what changed, why, and what remains blocked.",
        "Do not push owner-answer changes without verification and updated memory notes.",
        "owner_input_packet",
    ),
]


OWNER_REVIEW_PREP_ITEMS = [
    OwnerReviewPrepItem(
        "01",
        "Open the private preview with the access code.",
        "Confirm the owner can reach the gated site before the meeting starts.",
        "The meeting should feel composed, not technical.",
        "review_command_center",
    ),
    OwnerReviewPrepItem(
        "02",
        "Start from the command center.",
        "Use the command center as the table of contents instead of jumping through random pages.",
        "It keeps the review focused on flow, not route inventory.",
        "review_command_center",
    ),
    OwnerReviewPrepItem(
        "03",
        "Use the walkthrough for the first impression.",
        "Begin with the guided presentation before opening detailed planning pages.",
        "The owner should feel the vision before debating operations.",
        "owner_walkthrough",
    ),
    OwnerReviewPrepItem(
        "04",
        "Have the input packet and worksheet ready.",
        "Open the owner input packet and printable worksheet before asking for decisions.",
        "The meeting should end with captured answers, not vague approval.",
        "owner_input_packet",
    ),
    OwnerReviewPrepItem(
        "05",
        "Name the promise boundaries out loud.",
        "Say that pricing, dates, childcare, cafe, Foxtail, teen work, rentals, and full-campus availability are not public promises yet.",
        "This protects trust while still showing the full ecosystem.",
        "what_cultivate_is",
    ),
    OwnerReviewPrepItem(
        "06",
        "Close with the answer log and update plan.",
        "Show where answers will be recorded and how they become site changes.",
        "The owner can see that approvals will be handled carefully after the meeting.",
        "owner_answer_log",
    ),
]


OWNER_MEETING_SCRIPT = [
    OwnerMeetingScriptStep(
        "0-2 min",
        "Open with the purpose.",
        "This is a private concept review. The goal is to help the full Cultivate vision feel real while deciding what is safe to show families first.",
        "owner_review_prep",
        "Confirm the owner understands this is not public launch copy.",
        "Do not ask for pricing, schedule, or launch commitments in the opening.",
    ),
    OwnerMeetingScriptStep(
        "2-7 min",
        "Present the emotional center.",
        "Cultivate is strongest when it is framed as a whole-family place for belonging, real-life skills, parent breathing room, and community contribution.",
        "owner_walkthrough",
        "Watch for language the owner repeats or corrects.",
        "Do not over-explain every room before the owner feels the concept.",
    ),
    OwnerMeetingScriptStep(
        "7-10 min",
        "Name the safe first move.",
        "The recommended first move is a limited founding cohort, not a full-campus launch. That lets Cultivate test rhythm, trust, and demand before promising regulated or operationally heavy pieces.",
        "founding_cohort",
        "Ask whether the first-cohort frame feels right, too small, or too broad.",
        "Do not describe enrollment as open or the cohort as already approved.",
    ),
    OwnerMeetingScriptStep(
        "10-13 min",
        "Protect the promise boundaries.",
        "The full ecosystem can stay visible, but pricing, dates, childcare, cafe, Foxtail, paid teen work, rentals, and full-campus availability need owner approval or validation before public use.",
        "what_cultivate_is",
        "Mark any boundary the owner wants to revise.",
        "Do not soften the high-risk items into public promises during the meeting.",
    ),
    OwnerMeetingScriptStep(
        "13-20 min",
        "Move into owner answers.",
        "Now we need the answers only you can give: story, category wording, first cohort scope, schedule, pricing stance, day-one spaces, intake process, proof assets, and CTA.",
        "owner_input_packet",
        "Use the worksheet to mark Approved, Revise, Hold, or Validate.",
        "Do not rely on memory; write the answer or status down.",
    ),
    OwnerMeetingScriptStep(
        "20-25 min",
        "Close with the update path.",
        "After this meeting, answers go into the answer log first, then approvals and assumptions, then private draft pages. Public copy only moves after the gate is clear.",
        "post_meeting_update_plan",
        "Confirm the next artifact: revised copy, validation checklist, or held decision.",
        "Do not end with a vague next step.",
    ),
]


OWNER_MEETING_RECAP_ITEMS = [
    OwnerMeetingRecapItem(
        "Approved",
        "Record decisions the owner clearly approved.",
        "No approvals recorded yet. Move items here only after the owner confirms wording or scope.",
        "memory/08-owner-answer-log.md",
        "owner_answer_log",
    ),
    OwnerMeetingRecapItem(
        "Revise",
        "Capture concepts the owner likes but wants reworded or reshaped.",
        "No revision notes recorded yet. Use this for language, naming, audience, or offer changes.",
        "Owner review worksheet",
        "owner_review_worksheet",
    ),
    OwnerMeetingRecapItem(
        "Hold",
        "Name decisions that should stay private or unresolved.",
        "No holds recorded yet. Use this for items that should not appear in public drafts.",
        "Approval matrix",
        "approval_matrix",
    ),
    OwnerMeetingRecapItem(
        "Validate",
        "Turn operational uncertainty into evidence or checklist work.",
        "No validation tasks recorded yet. Use this for childcare, cafe, partnerships, teen work, rentals, pricing, dates, and facility details.",
        "Launch readiness",
        "launch_readiness",
    ),
    OwnerMeetingRecapItem(
        "Next Artifact",
        "Choose the next concrete file, page, or checklist to update.",
        "No next artifact selected yet. Choose one update target before ending the recap.",
        "Post-meeting update plan",
        "post_meeting_update_plan",
    ),
]


OWNER_REVIEW_PACKET_ITEMS = [
    OwnerReviewPacketItem(
        "Before",
        "Owner Review Prep",
        "Confirm access, meeting path, decision tools, and promise boundaries.",
        "A prepared review room.",
        "owner_review_prep",
    ),
    OwnerReviewPacketItem(
        "Before",
        "Owner Meeting Script",
        "Guide the facilitator through what to say, show, capture, and avoid.",
        "A calm meeting plan.",
        "owner_meeting_script",
    ),
    OwnerReviewPacketItem(
        "During",
        "Owner Walkthrough",
        "Present the concept visually before asking for operational decisions.",
        "Owner confidence and first reactions.",
        "owner_walkthrough",
    ),
    OwnerReviewPacketItem(
        "During",
        "Owner Input Packet",
        "Ask the owner-only questions that unblock public copy.",
        "Answers needed for story, scope, offer, proof, intake, and CTA.",
        "owner_input_packet",
    ),
    OwnerReviewPacketItem(
        "During",
        "Owner Review Worksheet",
        "Record approved, revise, hold, and validate statuses while talking.",
        "Meeting notes that do not rely on memory.",
        "owner_review_worksheet",
    ),
    OwnerReviewPacketItem(
        "After",
        "Owner Meeting Recap",
        "Summarize the meeting into approved, revise, hold, validate, and next-artifact buckets.",
        "A readable recap before site edits.",
        "owner_meeting_recap",
    ),
    OwnerReviewPacketItem(
        "After",
        "Owner Answer Log",
        "Move confirmed answers into the durable markdown/source-of-truth ledger.",
        "Logged owner answers.",
        "owner_answer_log",
    ),
    OwnerReviewPacketItem(
        "After",
        "Post-Meeting Update Plan",
        "Convert logged answers into app data, approvals, assumptions, drafts, tests, and memory updates.",
        "A safe update order.",
        "post_meeting_update_plan",
    ),
    OwnerReviewPacketItem(
        "After",
        "Approval Matrix",
        "Mark what is ready, blocked, internal, or validation-first before public copy changes.",
        "Updated publishing gate.",
        "approval_matrix",
    ),
    OwnerReviewPacketItem(
        "After",
        "Next Actions",
        "Turn owner answers into concrete artifacts and work queues.",
        "A clear next build pass.",
        "next_actions",
    ),
]


PUBLIC_DRAFT_ITEMS = [
    PublicDraftItem(
        "Home",
        "Explain Cultivate simply and warmly for families.",
        "Owner preview, brand voice, family journey, and ecosystem map.",
        "Owner approves the public category, first offer, and claims boundaries.",
        "Draft a public-safe hero, concept summary, and first-cohort call-to-action.",
        "draft_home",
    ),
    PublicDraftItem(
        "About",
        "Tell the why behind Cultivate without overdefining the operating model.",
        "Full ecosystem source, day-in-the-life narrative, and owner-approved language.",
        "Founder story, team language, and public mission wording are approved.",
        "Create a warm origin story and explain the village model.",
        "draft_about",
    ),
    PublicDraftItem(
        "Founding Cohort",
        "Describe the first safe launch shape.",
        "Founding cohort page, roadmap, launch readiness, and decision dashboard.",
        "Schedule, age scope, location assumptions, and intake process are approved.",
        "Turn the current recommendation into a family-facing draft.",
        "draft_cohort",
    ),
    PublicDraftItem(
        "FAQ",
        "Answer sensitive parent questions with calm precision.",
        "FAQ / Concern Lab and Brand Voice Lab.",
        "Exact answers for childcare, cafe, teen roles, pricing, and timeline are approved.",
        "Convert internal response patterns into public FAQ items.",
        "draft_faq",
    ),
    PublicDraftItem(
        "Interest",
        "Collect early family interest when the process is ready.",
        "Founding family interest draft, launch roadmap, and privacy rules.",
        "Privacy language, storage process, owner contact, and offer scope are approved.",
        "Enable a real form only after the owner approves intake operations.",
        "founding_family_interest",
    ),
]


DRAFT_NAV = (
    DraftNavItem("Hub", "public_draft_hub", "Private planning"),
    DraftNavItem("Home", "draft_home", "Draft"),
    DraftNavItem("About", "draft_about", "Draft"),
    DraftNavItem("Cohort", "draft_cohort", "Draft"),
    DraftNavItem("FAQ", "draft_faq", "Draft"),
    DraftNavItem("Interest", "founding_family_interest", "Disabled draft"),
)


PUBLISH_GATES = (
    PublishGateItem(
        "Category language",
        "Owner approval needed",
        "Confirm the public one-line description for what Cultivate is and who it serves first.",
        "brand_voice",
    ),
    PublishGateItem(
        "First offer scope",
        "Owner approval needed",
        "Confirm the founding cohort name, audience, schedule assumptions, and intake path.",
        "cohort_blueprint",
    ),
    PublishGateItem(
        "Claim boundaries",
        "Approval matrix check",
        "Keep pricing, dates, childcare, cafe, partner, paid teen work, rentals, and capacity out of public copy until validated.",
        "approval_matrix",
    ),
    PublishGateItem(
        "Operational validation",
        "Validate first",
        "Document the readiness path for sensitive pieces before they appear as available services.",
        "launch_readiness",
    ),
    PublishGateItem(
        "Intake and privacy",
        "Process needed",
        "Approve how family interest is collected, stored, followed up on, and described.",
        "founding_family_interest",
    ),
)


REVIEW_SURFACES = [
    ReviewSurface(
        "Start here",
        "Owner Walkthrough",
        "You want to present the full concept in one guided conversation.",
        "Does this feel like Cultivate?",
        "owner_walkthrough",
    ),
    ReviewSurface(
        "Start here",
        "Review Command Center",
        "You need a meeting dashboard that explains where to go next.",
        "What should we review today?",
        "review_command_center",
    ),
    ReviewSurface(
        "Start here",
        "Owner Review Packet",
        "You want the full before, during, and after owner-review sequence in one place.",
        "What is the complete review packet?",
        "owner_review_packet",
    ),
    ReviewSurface(
        "Start here",
        "Owner Brief",
        "You need the whole strategy in one concise owner-facing summary.",
        "What is the simple version of what we are building?",
        "owner_brief",
    ),
    ReviewSurface(
        "Start here",
        "Next Actions Board",
        "You need to turn the preview into a practical work queue.",
        "What do we do next?",
        "next_actions",
    ),
    ReviewSurface(
        "Experience",
        "Family Journey Map",
        "You want to understand the family path from first curiosity to belonging.",
        "What should a family feel at each stage?",
        "family_journey",
    ),
    ReviewSurface(
        "Experience",
        "A Day at Cultivate",
        "You want the concept to feel lived-in and practical.",
        "Does the rhythm feel calm, useful, and true?",
        "day_at_cultivate",
    ),
    ReviewSurface(
        "Planning",
        "Launch Roadmap",
        "You need sequence without inventing dates.",
        "What has to happen before public copy?",
        "launch_roadmap",
    ),
    ReviewSurface(
        "Planning",
        "Founding Cohort Blueprint",
        "You need the first term to feel operational without making public promises.",
        "What actually happens across the five-week test?",
        "cohort_blueprint",
    ),
    ReviewSurface(
        "Planning",
        "Impact Signals",
        "You need evidence from the first cohort to decide what to repeat or expand.",
        "How will we know the first term worked?",
        "impact_signals",
    ),
    ReviewSurface(
        "Planning",
        "Approval Matrix",
        "You need to decide which claims can move toward public use.",
        "What is approved, internal, or blocked?",
        "approval_matrix",
    ),
    ReviewSurface(
        "Planning",
        "Owner Decision Dashboard",
        "You want the next approval conversation to end with specific choices.",
        "Which decisions unlock the next build?",
        "owner_decisions",
    ),
    ReviewSurface(
        "Planning",
        "Owner Input Packet",
        "You need the exact questions that turn the private preview into approved public copy.",
        "What does the owner need to answer next?",
        "owner_input_packet",
    ),
    ReviewSurface(
        "Planning",
        "Owner Review Worksheet",
        "You want a printable note-taking surface for the owner conversation.",
        "Where do the answers get captured?",
        "owner_review_worksheet",
    ),
    ReviewSurface(
        "Planning",
        "Owner Answer Log",
        "You need a durable ledger of owner answers before changing public drafts.",
        "What has actually been approved?",
        "owner_answer_log",
    ),
    ReviewSurface(
        "Planning",
        "Post-Meeting Update Plan",
        "You need a safe order for converting owner answers into repo changes.",
        "What changes after the meeting?",
        "post_meeting_update_plan",
    ),
    ReviewSurface(
        "Planning",
        "Owner Review Prep",
        "You want to make the meeting polished before the owner sees the site.",
        "Are we ready to present?",
        "owner_review_prep",
    ),
    ReviewSurface(
        "Planning",
        "Owner Meeting Script",
        "You want facilitator notes for presenting the preview cleanly.",
        "What should we say in the meeting?",
        "owner_meeting_script",
    ),
    ReviewSurface(
        "Planning",
        "Owner Meeting Recap",
        "You need a structured summary after the owner review.",
        "What did we decide, hold, or validate?",
        "owner_meeting_recap",
    ),
    ReviewSurface(
        "Safety",
        "FAQ / Concern Lab",
        "You need careful responses to sensitive parent questions.",
        "How do we answer without overpromising?",
        "faq_lab",
    ),
    ReviewSurface(
        "Safety",
        "Source Evidence Room",
        "You want to trace site claims back to source documents.",
        "What is supported by the docs?",
        "source_evidence",
    ),
    ReviewSurface(
        "Safety",
        "Assumptions Review",
        "You want to see which working assumptions are safe and which need owner approval.",
        "What are we treating as true for now?",
        "assumptions_review",
    ),
    ReviewSurface(
        "Safety",
        "What Cultivate Is / Is Not",
        "You need public category clarity without overpromising regulated services.",
        "How do we explain Cultivate carefully?",
        "what_cultivate_is",
    ),
    ReviewSurface(
        "Future public",
        "Public Draft Hub",
        "You want to plan public pages before they are approved to publish.",
        "What page should be drafted next, and what must wait?",
        "public_draft_hub",
    ),
    ReviewSurface(
        "Future public",
        "Draft Home",
        "You want to see how the public homepage could feel after approval.",
        "Does this public-facing story feel clear and careful?",
        "draft_home",
    ),
    ReviewSurface(
        "Future public",
        "Draft About",
        "You want to preview the public origin story and village model.",
        "Does this explain why Cultivate exists without overdefining operations?",
        "draft_about",
    ),
    ReviewSurface(
        "Future public",
        "Draft Founding Cohort",
        "You want to preview how the first offer could be explained to families.",
        "Is the first cohort clear, bounded, and compelling?",
        "draft_cohort",
    ),
    ReviewSurface(
        "Future public",
        "Draft FAQ",
        "You want to preview public answers without approving them yet.",
        "Which answers are ready, and which need owner edits?",
        "draft_faq",
    ),
    ReviewSurface(
        "Build system",
        "Brand Voice",
        "You need copy to stay warm, grounded, and careful around unapproved promises.",
        "What should Cultivate sound like?",
        "brand_voice",
    ),
    ReviewSurface(
        "Build system",
        "Glossary",
        "You need shared definitions for names, spaces, and public-safe terms.",
        "What do these words mean right now?",
        "glossary",
    ),
    ReviewSurface(
        "Build system",
        "Why Cultivate",
        "You need a source-safe credibility layer for family pain points and the responsible first step.",
        "Why does this model matter?",
        "why_cultivate",
    ),
    ReviewSurface(
        "Build system",
        "UI Kitchen Sink",
        "You want to check reusable colors, type, buttons, cards, and page components.",
        "Does the system feel consistent?",
        "ui_kitchen_sink",
    ),
    ReviewSurface(
        "Build system",
        "UX Lab",
        "You want to prototype interaction ideas before they become public-facing pages.",
        "What should feel easier?",
        "ux_lab",
    ),
    ReviewSurface(
        "Build system",
        "Offer Model",
        "You want to explore offer buckets without turning them into pricing commitments.",
        "What might the ecosystem include?",
        "membership_model",
    ),
]


COMMAND_FLOW = (
    CommandStep(
        "01",
        "Walkthrough",
        "Show the vision in a guided, presentation-ready order.",
        "owner_walkthrough",
    ),
    CommandStep(
        "02",
        "Family Journey",
        "Make the experience feel human and easy to understand.",
        "family_journey",
    ),
    CommandStep(
        "03",
        "Approvals",
        "Separate safe language from claims that need owner signoff.",
        "approval_matrix",
    ),
    CommandStep(
        "04",
        "Next Actions",
        "Leave the meeting with concrete work, not loose enthusiasm.",
        "next_actions",
    ),
)


MEETING_TRACKS = (
    MeetingTrack(
        "15 minute review",
        "Impress first, then ask for shape approval.",
        "Use Walkthrough, Owner Brief, and Approvals when the owner has limited time and needs the cleanest strategic read.",
    ),
    MeetingTrack(
        "Working session",
        "Turn the concept into decisions.",
        "Use Actions, Roadmap, Blueprint, and Signals when the goal is to leave with assignments and validation work.",
    ),
    MeetingTrack(
        "Public page prep",
        "Separate draft copy from publishable claims.",
        "Use Drafts, FAQ Lab, Evidence, and Approvals before anything moves toward a public test domain.",
    ),
)


GUIDED_REVIEW_STEPS = (
    GuidedReviewStep(
        "01",
        "Preview",
        "Start with the full private concept and first-launch stance.",
        "owner_preview",
    ),
    GuidedReviewStep(
        "02",
        "Command",
        "Choose the right room and keep the owner review focused.",
        "review_command_center",
    ),
    GuidedReviewStep(
        "03",
        "Walkthrough",
        "Present the vision in a guided, meeting-ready order.",
        "owner_walkthrough",
    ),
    GuidedReviewStep(
        "04",
        "Brief",
        "Compress the concept, first move, holdbacks, and approval ask.",
        "owner_brief",
    ),
    GuidedReviewStep(
        "05",
        "Approvals",
        "Separate publishable language from claims that need validation.",
        "approval_matrix",
    ),
    GuidedReviewStep(
        "06",
        "Actions",
        "Turn the review into approvals, validation work, and next artifacts.",
        "next_actions",
    ),
)


PRIMARY_NAV = (
    NavItem("Preview", "owner_preview", ("owner_preview", "index")),
    NavItem("Command", "review_command_center"),
    NavItem("Brief", "owner_brief"),
    NavItem("Actions", "next_actions"),
    NavItem(
        "Drafts",
        "public_draft_hub",
        ("public_draft_hub", "draft_home", "draft_about", "draft_cohort", "draft_faq"),
    ),
    NavItem("Walkthrough", "owner_walkthrough"),
)


DIRECTORY_NAV = (
    NavSection(
        "Experience",
        (
            NavItem("Family Journey", "family_journey"),
            NavItem("A Day", "day_at_cultivate"),
            NavItem("Spaces", "spaces"),
            NavItem("Ecosystem", "ecosystem_map"),
        ),
    ),
    NavSection(
        "Planning",
        (
            NavItem("Roadmap", "launch_roadmap"),
            NavItem("Packet", "owner_review_packet"),
            NavItem("Cohort", "founding_cohort"),
            NavItem("Blueprint", "cohort_blueprint"),
            NavItem("Signals", "impact_signals"),
            NavItem("Readiness", "launch_readiness"),
            NavItem("Input Packet", "owner_input_packet"),
            NavItem("Worksheet", "owner_review_worksheet"),
            NavItem("Answer Log", "owner_answer_log"),
            NavItem("Update Plan", "post_meeting_update_plan"),
            NavItem("Prep", "owner_review_prep"),
            NavItem("Script", "owner_meeting_script"),
            NavItem("Recap", "owner_meeting_recap"),
        ),
    ),
    NavSection(
        "Safety",
        (
            NavItem("Approvals", "approval_matrix"),
            NavItem("Decisions", "owner_decisions"),
            NavItem("FAQ Lab", "faq_lab"),
            NavItem("Evidence", "source_evidence"),
            NavItem("Assumptions", "assumptions_review"),
            NavItem("Is / Is Not", "what_cultivate_is"),
        ),
    ),
    NavSection(
        "Build System",
        (
            NavItem("Voice", "brand_voice"),
            NavItem("Glossary", "glossary"),
            NavItem("Why", "why_cultivate"),
            NavItem("Offers", "membership_model"),
            NavItem("Interest", "founding_family_interest"),
            NavItem("Kitchen Sink", "ui_kitchen_sink"),
            NavItem("UX Lab", "ux_lab"),
        ),
    ),
)


APPROVAL_ITEMS = [
    ApprovalItem(
        "Cultivate is a homeschool family campus in Central Florida.",
        "Ready for owner review",
        "Owner-updated ecosystem source and current site strategy.",
        "Can become public-facing after owner confirms the exact category language.",
        "Approve or revise the category line.",
        "brand_voice",
    ),
    ApprovalItem(
        "A limited founding cohort is the safest first launch.",
        "Ready for owner review",
        "Founding cohort recommendation, launch readiness, roadmap, and decision dashboard.",
        "Can become public-facing only after scope, schedule, and intake process are approved.",
        "Approve first cohort label, age range, and term shape.",
        "founding_cohort",
    ),
    ApprovalItem(
        "The Summit is the current teen-space name.",
        "Needs confirmation",
        "Owner-updated naming direction; The Glade preserved as earlier-source provenance.",
        "Hold public naming until the owner confirms final name.",
        "Confirm The Summit or choose the final public teen-space name.",
        "owner_decisions",
    ),
    ApprovalItem(
        "The Sprout Space is a future childcare vision.",
        "Validate first",
        "Sprout Space source docs and readiness risk notes.",
        "Do not publish as available childcare, drop-off care, or preschool.",
        "Validate licensing, staffing, ratios, and teen-helper boundaries.",
        "launch_readiness",
    ),
    ApprovalItem(
        "The Harvest Cafe is a future teen-learning cafe vision.",
        "Validate first",
        "Harvest Cafe and Foxtail source docs.",
        "Do not publish cafe operation, coffee sales, or partner claims.",
        "Validate food-service path and partnership timing.",
        "faq_lab",
    ),
    ApprovalItem(
        "Teen contribution is part of the learning model.",
        "Internal only",
        "Ecosystem concept and concern-response guardrails.",
        "Public copy should avoid paid jobs, supervision, or employment claims.",
        "Define allowed teen responsibilities by age and supervision model.",
        "approval_matrix",
    ),
    ApprovalItem(
        "Pricing and launch dates are not ready.",
        "Blocked for public",
        "Membership model and roadmap rules.",
        "Do not publish prices, opening dates, or enrollment claims.",
        "Approve offer, schedule, cost model, and intake process first.",
        "membership_model",
    ),
]


APPROVAL_STATUS_GUIDE = (
    (
        "Ready for owner review",
        "Strong enough for the owner to approve, revise, or move toward public-safe copy.",
        "Ask for a yes, a wording edit, or a clear hold.",
    ),
    (
        "Needs confirmation",
        "Promising, but a specific naming or category choice still needs owner confirmation.",
        "Resolve the owner preference before public wording is drafted.",
    ),
    (
        "Validate first",
        "Important future vision, but operational, regulatory, or partnership details are not ready.",
        "Keep private and turn the issue into a validation checklist.",
    ),
    (
        "Internal only",
        "Useful for planning, but too sensitive or easy to misread as a public promise.",
        "Use internally and translate carefully only after boundaries are approved.",
    ),
    (
        "Blocked for public",
        "Do not publish until the owner approves the underlying business and operating details.",
        "Leave out of public pages until the block is removed.",
    ),
)


def build_approval_summaries(
    approvals: tuple[ApprovalItem, ...] | list[ApprovalItem],
) -> tuple[ApprovalSummary, ...]:
    counts = {status: 0 for status, _meaning, _next_move in APPROVAL_STATUS_GUIDE}
    for item in approvals:
        counts[item.status] = counts.get(item.status, 0) + 1
    return tuple(
        ApprovalSummary(status, counts.get(status, 0), meaning, next_move)
        for status, meaning, next_move in APPROVAL_STATUS_GUIDE
        if counts.get(status, 0)
    )


COHORT_BLOCKS = [
    CohortBlock(
        "Week 1",
        "Belonging and baseline",
        "Set community agreements, map strengths, and choose first responsibility lanes.",
        "Create project teams, learn the room rhythm, and make a simple personal skills map.",
        "Share family needs, work rhythms, possible contributions, and practical constraints.",
        "Family intake themes, skills inventory, attendance comfort, and first impressions.",
    ),
    CohortBlock(
        "Week 2",
        "Food, care, and hospitality",
        "Practice hosting, planning, cleanup, budgeting language, and shared care without cafe claims.",
        "Plan a snack/lunch rhythm, assign helpful roles, and document what makes a space feel welcoming.",
        "Observe flow, identify food allergies/preferences, and note operational friction.",
        "Hospitality reflections, supply list, adult supervision needs, and food-service questions.",
    ),
    CohortBlock(
        "Week 3",
        "Making, repair, and useful work",
        "Lead or support a real build/repair/making task with clear adult guardrails.",
        "Complete a hands-on project that can be displayed on the Village Wall.",
        "Offer skills, tools, stories, or project mentorship where appropriate.",
        "Project artifacts, confidence notes, facilitator observations, and parent contributions.",
    ),
    CohortBlock(
        "Week 4",
        "Outdoor rhythm and stewardship",
        "Test garden, outdoor setup, stewardship, or nature-based project responsibilities lightly.",
        "Explore simple outdoor care, observation, and movement activities if the site allows.",
        "Name access, safety, shade, supervision, and weather realities.",
        "Outdoor feasibility notes, supervision ratios, safety concerns, and family enthusiasm.",
    ),
    CohortBlock(
        "Week 5",
        "Showcase and next-shape",
        "Present work, reflect on responsibility, and name what they want more of next term.",
        "Share projects, skills learned, and what helped them feel confident.",
        "Give structured feedback on rhythm, value, schedule, communication, and trust.",
        "Showcase artifacts, feedback themes, retention interest, and owner next-step decisions.",
    ),
]


IMPACT_SIGNALS = [
    ImpactSignal(
        "Belonging",
        "Cultivate only works if kids and parents feel known, safe, and wanted.",
        "Short weekly reflection prompts, facilitator notes, and parent check-ins.",
        "Weekly during the first cohort.",
        "Whether the rhythm is emotionally strong enough to repeat.",
    ),
    ImpactSignal(
        "Useful skill growth",
        "The promise is real-life skills, so evidence should show practice, not grades.",
        "Project artifacts, before/after skill notes, photos, and participant self-reflection.",
        "At project start, project close, and final showcase.",
        "Which skill blocks should become core programming.",
    ),
    ImpactSignal(
        "Parent relief",
        "The Grove matters if parents actually gain breathing room, work time, or community.",
        "Parent pulse checks, workspace usage notes, and observed contribution patterns.",
        "Midpoint and final week.",
        "Whether parent workspace/community becomes a priced offer or member benefit.",
    ),
    ImpactSignal(
        "Operational load",
        "A beautiful concept has to be manageable for staff, space, supplies, and transitions.",
        "Daily friction log, supply usage, transition timing, and facilitator debriefs.",
        "After each cohort session.",
        "What must be simplified before a second term.",
    ),
    ImpactSignal(
        "Validation blockers",
        "Childcare, cafe, teen roles, rentals, and outdoor campus need separate validation paths.",
        "Track unresolved questions in the approval matrix and readiness dashboard.",
        "Owner review at the end of each week.",
        "Which future vision item is ready for deeper validation next.",
    ),
]


BRIEF_SECTIONS = [
    BriefSection(
        "Concept",
        "Cultivate is a homeschool family campus.",
        "The strongest current frame is a whole-family campus for real-life skills, belonging, parent breathing room, and community contribution.",
        "Owner preview, source evidence, brand voice, and ecosystem map.",
    ),
    BriefSection(
        "First move",
        "Launch a limited founding cohort before the full campus.",
        "The safest first version tests teen belonging, middle-kid projects, parent workspace, workshops, and reflection without depending on regulated or unvalidated pieces.",
        "Founding cohort, cohort blueprint, launch readiness, and approval matrix.",
    ),
    BriefSection(
        "Hold back",
        "Keep sensitive claims internal until validated.",
        "Childcare, cafe operation, Foxtail, paid teen work, public rentals, pricing, dates, and full outdoor campus should stay private or future-vision until approved.",
        "FAQ lab, approval matrix, launch roadmap, and public draft hub.",
    ),
    BriefSection(
        "Owner decision",
        "The next approval is shape, not launch.",
        "The owner does not need to approve every future phase now. The important next approval is the first-cohort frame and what can move into public-safe draft copy.",
        "Owner decisions, review command center, and next actions.",
    ),
]


NEXT_ACTIONS = [
    NextAction(
        "Owner approval",
        "Confirm the public category line for Cultivate.",
        "Everything public depends on whether the owner approves the homeschool family campus framing.",
        "Approved or revised one-sentence category statement.",
        "brand_voice",
    ),
    NextAction(
        "Owner approval",
        "Confirm the first cohort label, audience, and rough term shape.",
        "The founding cohort is the safest first launch, but it still needs an approved public frame.",
        "Approved first-cohort scope for public draft work.",
        "cohort_blueprint",
    ),
    NextAction(
        "Validation",
        "Create the childcare and teen-helper validation checklist.",
        "The Sprout Space is powerful but should not move into public claims without licensing and supervision clarity.",
        "Internal checklist for childcare path, ratios, staff, and teen boundaries.",
        "launch_readiness",
    ),
    NextAction(
        "Validation",
        "Hold cafe and Foxtail language until the food-service path is clearer.",
        "Cafe language can quickly sound like an operating promise or partnership claim.",
        "Approved internal stance for Harvest Cafe and partnership timing.",
        "faq_lab",
    ),
    NextAction(
        "Web build",
        "Draft the private public-safe Home page next.",
        "The site now has enough strategy, voice, journey, and approval structure to produce a careful first public draft.",
        "Private `/draft-home` or equivalent page, still gated and unlaunched.",
        "public_draft_hub",
    ),
    NextAction(
        "Evidence",
        "Define the first-cohort evidence packet.",
        "The first term should end with artifacts, feedback, and signals that guide expansion.",
        "Cohort recap outline and weekly evidence prompts.",
        "impact_signals",
    ),
]


ACTION_LANE_GUIDE = (
    (
        "Owner approval",
        "Decisions the owner can make before deeper validation begins.",
        "Ask for approval, revision, or a deliberate hold.",
    ),
    (
        "Validation",
        "Sensitive pieces that need operating clarity before public copy.",
        "Turn each item into a checklist or owner-reviewed stance.",
    ),
    (
        "Web build",
        "Private site artifacts that can be drafted without publishing.",
        "Build the next gated page and keep it tied to approval rules.",
    ),
    (
        "Evidence",
        "Signals and artifacts that make the first cohort useful.",
        "Define the packet before the cohort starts.",
    ),
)


def build_action_lane_summaries(
    actions: tuple[NextAction, ...] | list[NextAction],
) -> tuple[ActionLaneSummary, ...]:
    counts = {lane: 0 for lane, _purpose, _next_move in ACTION_LANE_GUIDE}
    for action in actions:
        counts[action.lane] = counts.get(action.lane, 0) + 1
    return tuple(
        ActionLaneSummary(lane, counts.get(lane, 0), purpose, next_move)
        for lane, purpose, next_move in ACTION_LANE_GUIDE
        if counts.get(lane, 0)
    )


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-only-secret")
    app.config["PREVIEW_ACCESS_CODE"] = os.environ.get(
        "CULTIVATE_PREVIEW_ACCESS_CODE", "cultivate-preview"
    )
    app.config["PREVIEW_PUBLIC"] = os.environ.get("CULTIVATE_PREVIEW_PUBLIC") == "1"

    @app.context_processor
    def inject_navigation():
        current_route = request.endpoint
        guided_current = None
        guided_previous = None
        guided_next = None
        draft_current = None
        for index, step in enumerate(GUIDED_REVIEW_STEPS):
            if step.route == current_route:
                guided_current = step
                if index > 0:
                    guided_previous = GUIDED_REVIEW_STEPS[index - 1]
                if index + 1 < len(GUIDED_REVIEW_STEPS):
                    guided_next = GUIDED_REVIEW_STEPS[index + 1]
                break
        for item in DRAFT_NAV:
            if item.route == current_route:
                draft_current = item
                break
        return {
            "directory_nav": DIRECTORY_NAV,
            "draft_current": draft_current,
            "draft_nav": DRAFT_NAV,
            "guided_current": guided_current,
            "guided_next": guided_next,
            "guided_previous": guided_previous,
            "guided_review_steps": GUIDED_REVIEW_STEPS,
            "primary_nav": PRIMARY_NAV,
            "publish_gates": PUBLISH_GATES,
        }

    @app.before_request
    def preview_gate():
        if request.endpoint in {"healthz", "static"}:
            return None
        if app.config["PREVIEW_PUBLIC"]:
            return None
        access_code = app.config["PREVIEW_ACCESS_CODE"]
        if not access_code:
            return None
        if request.args.get("access") == access_code:
            session["preview_ok"] = True
            return redirect(request.path)
        if session.get("preview_ok"):
            return None
        return render_template("access.html"), 401

    @app.get("/healthz")
    def healthz():
        return {"ok": True, "service": "cultivate-web"}

    @app.get("/")
    @app.get("/owner-preview")
    def owner_preview():
        return render_template("owner_preview.html", spaces=SPACES)

    @app.get("/owner-review-packet")
    def owner_review_packet():
        return render_template(
            "owner_review_packet.html", packet_items=OWNER_REVIEW_PACKET_ITEMS
        )

    @app.get("/ui-kitchen-sink")
    def ui_kitchen_sink():
        return render_template("ui_kitchen_sink.html", spaces=SPACES)

    @app.get("/ux-lab")
    def ux_lab():
        return render_template("ux_lab.html", spaces=SPACES)

    @app.get("/ecosystem-map")
    def ecosystem_map():
        return render_template("ecosystem_map.html", spaces=SPACES)

    @app.get("/spaces")
    def spaces():
        return render_template("spaces.html", spaces=SPACES)

    @app.get("/founding-cohort")
    def founding_cohort():
        return render_template("founding_cohort.html")

    @app.get("/launch-readiness")
    def launch_readiness():
        return render_template("launch_readiness.html", readiness=READINESS)

    @app.get("/day-at-cultivate")
    def day_at_cultivate():
        return render_template("day_at_cultivate.html", moments=DAY_MOMENTS)

    @app.get("/brand-voice")
    def brand_voice():
        return render_template("brand_voice.html", voice_pairs=VOICE_PAIRS)

    @app.get("/membership-model")
    def membership_model():
        return render_template("membership_model.html", offers=OFFER_BUCKETS)

    @app.get("/founding-family-interest")
    def founding_family_interest():
        return render_template("founding_family_interest.html")

    @app.get("/owner-decisions")
    def owner_decisions():
        return render_template(
            "owner_decisions.html",
            decision_risk_summaries=build_decision_risk_summaries(DECISIONS),
            decisions=DECISIONS,
        )

    @app.get("/owner-input-packet")
    def owner_input_packet():
        return render_template(
            "owner_input_packet.html", input_items=OWNER_INPUT_ITEMS
        )

    @app.get("/owner-review-worksheet")
    def owner_review_worksheet():
        return render_template(
            "owner_review_worksheet.html", input_items=OWNER_INPUT_ITEMS
        )

    @app.get("/owner-answer-log")
    def owner_answer_log():
        return render_template(
            "owner_answer_log.html", input_items=OWNER_INPUT_ITEMS
        )

    @app.get("/post-meeting-update-plan")
    def post_meeting_update_plan():
        return render_template(
            "post_meeting_update_plan.html", updates=POST_MEETING_UPDATES
        )

    @app.get("/owner-review-prep")
    def owner_review_prep():
        return render_template(
            "owner_review_prep.html", prep_items=OWNER_REVIEW_PREP_ITEMS
        )

    @app.get("/owner-meeting-script")
    def owner_meeting_script():
        return render_template(
            "owner_meeting_script.html", script_steps=OWNER_MEETING_SCRIPT
        )

    @app.get("/owner-meeting-recap")
    def owner_meeting_recap():
        return render_template(
            "owner_meeting_recap.html", recap_items=OWNER_MEETING_RECAP_ITEMS
        )

    @app.get("/owner-walkthrough")
    def owner_walkthrough():
        return render_template("owner_walkthrough.html", slides=WALKTHROUGH_SLIDES)

    @app.get("/family-journey")
    def family_journey():
        return render_template("family_journey.html", journey_steps=JOURNEY_STEPS)

    @app.get("/launch-roadmap")
    def launch_roadmap():
        return render_template("launch_roadmap.html", roadmap=ROADMAP_PHASES)

    @app.get("/faq-lab")
    def faq_lab():
        return render_template("faq_lab.html", concerns=CONCERN_ITEMS)

    @app.get("/source-evidence")
    def source_evidence():
        return render_template("source_evidence.html", evidence=EVIDENCE_ITEMS)

    @app.get("/why-cultivate")
    def why_cultivate():
        return render_template("why_cultivate.html", pain_points=PAIN_POINTS)

    @app.get("/glossary")
    def glossary():
        return render_template("glossary.html", terms=GLOSSARY_TERMS)

    @app.get("/what-cultivate-is")
    def what_cultivate_is():
        return render_template(
            "what_cultivate_is.html", comparisons=COMPARISON_ITEMS
        )

    @app.get("/assumptions-review")
    def assumptions_review():
        return render_template(
            "assumptions_review.html", assumptions=ASSUMPTION_ITEMS
        )

    @app.get("/public-draft-hub")
    def public_draft_hub():
        return render_template("public_draft_hub.html", drafts=PUBLIC_DRAFT_ITEMS)

    @app.get("/review-command-center")
    def review_command_center():
        return render_template(
            "review_command_center.html",
            command_flow=COMMAND_FLOW,
            meeting_tracks=MEETING_TRACKS,
            surfaces=REVIEW_SURFACES,
        )

    @app.get("/approval-matrix")
    def approval_matrix():
        return render_template(
            "approval_matrix.html",
            approval_summaries=build_approval_summaries(APPROVAL_ITEMS),
            approvals=APPROVAL_ITEMS,
        )

    @app.get("/cohort-blueprint")
    def cohort_blueprint():
        return render_template("cohort_blueprint.html", cohort_blocks=COHORT_BLOCKS)

    @app.get("/impact-signals")
    def impact_signals():
        return render_template("impact_signals.html", signals=IMPACT_SIGNALS)

    @app.get("/owner-brief")
    def owner_brief():
        return render_template("owner_brief.html", brief_sections=BRIEF_SECTIONS)

    @app.get("/next-actions")
    def next_actions():
        return render_template(
            "next_actions.html",
            action_lane_summaries=build_action_lane_summaries(NEXT_ACTIONS),
            actions=NEXT_ACTIONS,
        )

    @app.get("/draft-home")
    def draft_home():
        return render_template("draft_home.html", spaces=SPACES)

    @app.get("/draft-about")
    def draft_about():
        return render_template("draft_about.html")

    @app.get("/draft-cohort")
    def draft_cohort():
        return render_template("draft_cohort.html", cohort_blocks=COHORT_BLOCKS)

    @app.get("/draft-faq")
    def draft_faq():
        return render_template("draft_faq.html", concerns=CONCERN_ITEMS)

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="127.0.0.1", port=port, debug=True)
