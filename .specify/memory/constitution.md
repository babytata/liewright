<!--
Sync Impact Report
==================
Version change: (none / template) → 1.0.0
Modified principles: N/A (initial fill from template)
Added sections: None
Removed sections: None
Templates:
  - .specify/templates/plan-template.md ✅ (Constitution Check is generic; no update required)
  - .specify/templates/spec-template.md ✅ (scope/requirements align; no update required)
  - .specify/templates/tasks-template.md ✅ (task types compatible; no update required)
  - .cursor/commands/*.md ✅ (no CLAUDE-only references; commands live in .cursor/commands/)
Follow-up TODOs: None. RATIFICATION_DATE set to first-adoption date (same as Last Amended).
-->

# Liewright Constitution

## Core Principles

### I. User-First & Accessibility

Pages MUST be usable on common viewports and readable without relying on color alone. Critical
actions MUST be reachable via keyboard and work with standard assistive patterns. Rationale:
Liewright is a public-facing site; inclusive design is non-negotiable for trust and reach.

### II. Consistent UI & Brand

All pages MUST share the same navigation, header, and visual language (e.g. dark theme, Segoe UI,
container max-width, border and color tokens). New pages MUST reuse existing layout and style
patterns unless a documented exception is approved. Rationale: Consistency reduces cognitive load
and maintains a single recognizable Liewright identity.

### III. Security & Privacy by Default

User data and form submissions MUST be handled so that sensitive data is not logged or exposed.
Privacy-critical flows (e.g. contact, subscribe) MUST align with the stated privacy policy pages.
New features that collect or process personal data MUST be reviewed for compliance before merge.
Rationale: The site includes privacy policies and forms; trust requires matching behavior.

### IV. Testable Behavior

User-facing behavior and critical paths (e.g. form submission, redirects, error handling) MUST be
verifiable. When specs or plans require tests, tests MUST be written and failing before
implementation; then implementation MUST satisfy them. Rationale: Prevents regressions and
documents intended behavior as the project grows.

### V. Simplicity & Maintainability

Prefer plain PHP and minimal dependencies unless a concrete need is documented. Avoid
over-abstraction and speculative features (YAGNI). New dependencies or architectural complexity
MUST be justified in the implementation plan. Rationale: Keeps the codebase understandable and
easy to change for a small-site context.

## Technology & Stack

- **Runtime**: PHP (version to be pinned in plan per environment).
- **Front-end**: HTML/CSS in page scope; shared styles and structure reused across pages.
- **Server**: Apache (htaccess present); deployment and hosting constraints documented in
  feature plans where relevant.
- **Testing**: Approach defined per feature; when tests are required, use project-standard paths
  (e.g. tests/ unit or integration as per plan).

## Development Workflow

- New features MUST be specified (e.g. via speckit.specify) with user scenarios and acceptance
  criteria before implementation.
- Implementation plans MUST pass the Constitution Check (plan-template) before Phase 0 research.
- Code changes MUST preserve consistent UI and brand unless the spec explicitly allows
  divergence.
- Privacy- or security-sensitive changes MUST be reviewed for alignment with this constitution
  and existing privacy policy content.

## Governance

- This constitution supersedes ad-hoc practices for scope, principles, and workflow described
  here.
- **Amendments**: Changes require updating this file, incrementing the version (semantic:
  MAJOR = backward-incompatible principle removal/redefinition; MINOR = new principle or
  section; PATCH = clarifications/typos), and updating the Sync Impact Report at the top.
- **Compliance**: All PRs and feature plans MUST verify compliance with the principles above.
  Exceptions MUST be documented in the plan’s Complexity Tracking with justification.
- **Guidance**: Use feature specs, plan.md, and (when present) README or docs/quickstart.md for
  runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-02-15 | **Last Amended**: 2026-02-15
