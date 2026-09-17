# Question Bank — DevOps / Platform Engineering

> Reusable question pool. Difficulty markers: 🟢 base · 🟡 intermediate · 🔴 advanced.
> Prefer open, behavioural questions grounded in past experience. For every question,
> if the candidate does not give a concrete example, ask: *"Can you give me a specific
> example from your experience?"*
>
> Rebuild the token-efficient index after editing this file: `hiring index`.

## Index

- Behavioural — always the same
- Problem Solving & Logic
- CI/CD & Automation
- IaC — Terraform / Ansible
- AWS & Cloud
- Containers & Orchestration
- Monitoring & Observability
- Linux & Scripting
- Platform Engineering & Developer Experience
- AI & Modern Tooling
- Scenario-based
- Technical Exercises

---

## Behavioural — always the same

- 🟢 *"Tell me about a concrete experience where you worked beyond the traditional boundaries of your role. What was the context, what did you take on, and what result did you achieve?"*
- 🟢 *"Tell me how you chose and explored a professional topic over the last three months. What did you concretely do, and how did you verify what you learned?"*
- 🟢 *"Tell me about a situation where you collaborated with someone you had a difficult relationship with. How did you handle it, and what result did you reach together?"*
- 🟡 *"Describe a time you disagreed with a technical decision. How did you raise it, and what was the outcome?"*
- 🟡 *"Tell me about a mistake you made that had a real impact. How did you handle it and what changed in how you work afterwards?"*
- 🔴 *"Describe a situation where you drove an improvement no one asked you for. What made you start, and how did you get others on board?"*

## Problem Solving & Logic

- 🟢 *"Walk me through how you approach a problem you have never seen before. Use a real example."*
- 🟡 *"Tell me about the hardest bug or incident you diagnosed. How did you isolate the cause?"*
- 🟡 *"Describe a time you had to make a decision with incomplete information. How did you proceed?"*
- 🔴 *"You inherit a system you do not understand and something is failing intermittently. What is your first week?"*

## CI/CD & Automation

- 🟢 *"Describe a CI/CD pipeline you worked on directly. Which stages did it include, why were they necessary, and which part did you personally build or modify?"*
- 🟢 *"Tell me how you handled secrets in a pipeline, without sharing values or confidential details. Which risks did you consider and which controls did you apply?"*
- 🟡 *"Tell me about a concrete decision on what logic to put in the pipeline versus in the application or build scripts. Which criteria did you use?"*
- 🟡 *"Describe how you would structure pipeline stages for a monorepo with several deployable services."*
- 🔴 *"Tell me about a delivery-process improvement you measured. Which metrics (including DORA) did you choose, why, and what changed after your intervention?"*
- 🔴 *"A pipeline is flaky and the team started ignoring failures. How do you restore trust in it?"*

## IaC — Terraform / Ansible

- 🟢 *"Tell me about a task where you used Terraform or another IaC tool. What problem did it address, what did you contribute, and how did you verify changes before applying them?"*
- 🟡 *"Describe how you would manage state, concurrency and secrets in a Terraform workflow used by multiple people and a CI/CD pipeline."*
- 🟡 *"Compare a module-based Terraform layout with a flat one, using a context where you would choose each."*
- 🟡 *"Tell me how you keep Ansible playbooks idempotent and testable."*
- 🔴 *"You must refactor a large Terraform codebase with drift between state and reality. How do you approach it safely?"*

## AWS & Cloud

- 🟢 *"Describe how you would use a VPC and its components to isolate a simple application."*
- 🟡 *"Apply the shared-responsibility model to a cloud service you know: what stays with the provider and what with the customer?"*
- 🟡 *"Compare security groups and NACLs using a concrete network scenario."*
- 🟡 *"Tell me how you would evaluate a request to double the memory of a cloud microservice. What information would you gather?"*
- 🔴 *"Describe a cloud cost problem you investigated. How did you find the driver and what did you change?"*

## Containers & Orchestration

- 🟢 *"Describe the relationship between a Docker image and a running container. When does distinguishing them matter in practice?"*
- 🟡 *"Describe a situation where you would use a multi-stage build. Which problem does it solve?"*
- 🟡 *"Compare ENTRYPOINT and CMD with a concrete example. How do you choose?"*
- 🟡 *"Tell me how you would debug a container that keeps restarting in production."*
- 🔴 *"When would you introduce Kubernetes, and when is it overkill? Use a real trade-off."*

## Monitoring & Observability

- 🟢 *"Describe a technical investigation where metrics, logs or traces gave you different information. How did you choose which signal to analyze?"*
- 🟢 *"Tell me about your experience with a monitoring and alerting system. What did you contribute to metrics, dashboards, alerts and escalation?"*
- 🟡 *"How do you design an alert that is actionable and does not create fatigue?"*
- 🔴 *"You are asked to define SLOs for a service. How do you pick the indicators and targets?"*

## Linux & Scripting

- 🟢 *"Tell me about a task you automated with a shell or Python script. What did it replace?"*
- 🟡 *"Describe how you would investigate a Linux host that is running out of disk or memory."*
- 🟡 *"How do you make a script safe to run repeatedly and safe to fail halfway?"*
- 🔴 *"Walk me through diagnosing a process consuming CPU with no obvious cause."*

## Platform Engineering & Developer Experience

- 🟢 *"Tell me about an internal tool or platform you built or improved. Who were the users and what changed for them?"*
- 🟡 *"How do you decide what to make self-service versus what to keep gated?"*
- 🟡 *"Describe how you gathered feedback from developers to prioritize platform work."*
- 🔴 *"You must design an internal developer platform from scratch. What are the first three capabilities and why?"*

## AI & Modern Tooling

- 🟢 *"What role have AI tools played so far in your work or learning? If you haven't used them, how did you evaluate that choice?"*
- 🟡 *"Tell me about a task where you evaluated whether to use an AI tool. How did you decide and how did you verify the result?"*
- 🟡 *"What benefits and limits do you see in using AI for DevOps or infrastructure work?"*
- 🔴 *"How would you integrate AI assistance into a team's workflow without eroding review quality?"*

## Scenario-based

- 🔴 *"A cross-cutting change removed write permissions on a production folder used by a containerized service, and you do not have root. The call ends in 10 minutes. How do you handle it from the first minute to resolution?"*
- 🔴 *"A deploy went out and error rates rose slowly over 20 minutes. Walk me through your response."*
- 🔴 *"Two teams disagree on who owns a shared pipeline that keeps breaking. How do you unblock delivery?"*

## Technical Exercises

| Exercise | Topic | Difficulty | Time (min) |
|----------|-------|-----------|-----------|
| Run PostgreSQL container with a host volume | Containers | easy | 10 |
| Multi-stage Docker build to shrink an image | Containers | medium | 10 |
| Terraform module that outputs an instance's private DNS | Terraform | medium | 15 |
| Terraform local provider basics | Terraform | easy | 10 |
| Create a directory idempotently with Ansible | Ansible | easy | 5 |
| Linux navigation and file operations | Linux | easy | 5 |
| Git branching and commit verification | Git | easy | 5 |
| Pipeline & registry migration reasoning | Reasoning | advanced | 20 |
| Maximum product of three integers (Python) | Programming | medium | 15 |

---

## Log

- Initial generic question bank.
