# Preparazione Colloquio — {{CANDIDATE_NAME}}

> **Calibrazione**: profilo **{{SENIORITY_LABEL}}**. Focus su: {{SENIORITY_FOCUS}}
> Per ogni domanda personalizzata aggiungi un blocco `> **Risposta attesa**:` con
> indicatori ✅ Buona / ⚠️ Debole / 🚫 Red flag e un blocco `> **Follow-up di esempio**:`
> con 1-2 domande di approfondimento da usare se la risposta è vaga, opinionata,
> teorica o incompleta.

---

## Introduzione (intervistatore, ~3 min)

- Avvia la registrazione (con consenso) e condividi il link all'editor collaborativo / esercizi.
- Dai il benvenuto e presentati: il tuo ruolo e a chi rispondi.
- Presentazione azienda breve e fattuale. **Non** chiedere al candidato di recitare
  informazioni sull'azienda: valuta la motivazione autentica.

### Conoscenza spontanea e motivazione — prima della presentazione aziendale

1. *"Cosa sai già di noi e cosa ha catturato la tua attenzione?"*
2. *"Cosa ti ha portato ad accettare questo colloquio e quale aspetto della posizione vorresti esplorare?"*
3. *"Cosa cerchi nel tuo prossimo ruolo e cosa vorresti cambiare rispetto alla situazione attuale?"*

> **Nota**: non è un test di nozioni. Valuta preparazione di base, motivazione
> autentica e chiarezza delle aspettative. Se il recruiter ha condiviso poche
> informazioni, non penalizzare il candidato; osserva le domande che pone.

### Istruzioni per il candidato (da comunicare, non da chiedere)

1. Se una domanda non è chiara, chiedi subito — le domande di chiarimento sono benvenute.
2. Risposte concise e al punto: 1-2 minuti per domanda, max 3 se complessa.
   Dettagli concreti ed esempi specifici, non storie lunghe.

---

## Profilo sintetico

| Campo | Valore |
|-------|--------|
| **Nome** | {{CANDIDATE_NAME}} |
| **Ubicazione** | <!-- AGENT-FILL: profile_location | Dal CV: ubicazione del candidato. --> |
| **Esperienza totale** | <!-- AGENT-FILL: profile_total_exp | Dal CV: anni totali di esperienza. --> |
| **Esperienza DevOps/Platform** | <!-- AGENT-FILL: profile_devops_exp | Dal CV: anni in ruoli DevOps/SRE/Platform. --> |
| **Ruolo attuale** | <!-- AGENT-FILL: profile_role | Dal CV: ruolo/titolo attuale. --> |
| **Inglese (dichiarato)** | <!-- AGENT-FILL: profile_english | Dal CV: livello di inglese dichiarato. --> |
| **Data analisi** | {{DATE}} |
| **Stato** | `CV screening` / `Career path review` / `Structured interview` / `Work sample` / `Evidence review` / `HR checks pending` / `Final decision` / `Closed` |

### Copertura Must-Have / Nice-to-Have

<!-- AGENT-FILL: coverage | Valuta il CV contro le liste must-have e nice-to-have in ../profile.md. Produci due checklist (✅ coperto / ⚠️ parziale / ❌ mancante) con una riga di motivazione ciascuna. -->

### Flag analysis

<!-- AGENT-FILL: flags | Compila quattro tabelle brevi dal CV: 🔴 Red flags (possibili blocchi), 🟡 Yellow flags (da monitorare), 🟢 Green flags (punti forti reali), ❌ Nice-to-have mancanti. Una riga per voce. -->

---

## Parte 1 — Warmup (~25 min)

**Percorso professionale** (domande CV-based con livelli):

<!-- AGENT-FILL: cv_warmup_questions | Genera 3-5 domande comportamentali neutrali basate sul CV. Ognuna con un livello (🟢/🟡/🔴), il testo della domanda, un blocco "> **Risposta attesa**:" (✅/⚠️/🚫) e un blocco "> **Follow-up di esempio**:" con 2 follow-up di approfondimento. Focus su timeline, ownership reale vs esecuzione, gap o incongruenze del CV. Invita ad anonimizzare aziende, clienti e sistemi. -->

**Motivazione e fit** (ricorrenti — adattare al profilo):

- 🟢 *"Raccontami un'esperienza concreta in cui hai lavorato oltre i confini tradizionali del tuo ruolo. Qual era il contesto, quali responsabilità hai preso e quale risultato hai ottenuto?"*
  > **Follow-up di esempio**:
  > - "Quale parte hai trovato più difficile?"
  > - "Cosa avresti preferito delegare a un collega?"
- 🟢 *"Perché vuoi entrare e cosa ti aspetti da questo ruolo, dal team e dal tuo prossimo lavoro?"*
  > **Risposta attesa**: ✅ motivazione concreta allineata al ruolo, aspettative realistiche e verificabili; ⚠️ interesse guidato solo da brand/relocation/stipendio; 🚫 aspettative vaghe o disallineate.
  > **Follow-up di esempio**:
  > - "Se il lavoro risultasse diverso dalle tue aspettative su un aspetto chiave, come lo vivresti?"

<!-- AGENT-FILL: motivation_fit_questions | Aggiungi 1-2 domande comportamentali di fit basate sul CV, con risposta attesa. Evita sì/no, leading e formulazioni orientate a un esito positivo. Aggiungi sotto ciascuna un blocco "> **Follow-up di esempio**:". -->

**Profondità e self-awareness**:

- 🟡 *"Scegli due o tre tecnologie in cui senti di avere più esperienza. Per ognuna, raccontami l'ultimo problema complesso affrontato, cosa hai contribuito personalmente e cosa hai imparato."*
  > **Risposta attesa**: test di self-awareness. Una buona risposta distingue profondità reale da esposizione. Red flag se elenca tutto il CV.

<!-- AGENT-FILL: depth_questions | Aggiungi 1-2 domande neutrali per verificare la profondità o chiarire incongruenze del CV. Niente domande-trappola e nessuna insinuazione di esagerazione; chiedi contesto, contributo personale ed evidenze osservabili. -->

---

## Parte 2 — Technical deep dive (~25-30 min)

### Domande tecniche comuni (adattare al livello)

**Terraform / IaC — primo stack tecnico:**
- 🟢 *"Raccontami un task in cui hai usato Terraform o un altro strumento IaC. Quale problema risolveva, cosa hai contribuito e come verificavi le modifiche prima di applicarle?"*
  > **Risposta attesa**: esperienza con codice versionato, review, plan/test, gestione ambienti e apply controllato. Senza esperienza diretta, distinguere chiaramente teoria, strumenti equivalenti e piano di apprendimento.
- 🟡 *"Come gestiresti stato, concorrenza e secret in un workflow Terraform usato da più persone e da una pipeline CI/CD?"*
  > **Risposta attesa**: remote state protetto, locking, separazione ambienti, least privilege, secret manager. 🚫 state locale condiviso, `-lock=false`, secret nel repo.

**Filosofia e cultura DevOps:**
- 🟢 *"Raccontami un'esperienza concreta che rappresenta come applichi il DevOps quotidianamente. Qual era il contesto e cosa hai contribuito?"*
- 🟡 *"Descrivi una situazione in cui hai identificato o gestito debito tecnico. Come lo hai distinto da un difetto visibile al cliente e come hai deciso la priorità?"*

**CI/CD:**
- 🟢 *"Descrivi una pipeline CI/CD su cui hai lavorato direttamente. Quali stage includeva, perché erano necessari e quale parte hai costruito o modificato?"*
- 🔴 *"Raccontami un miglioramento del processo di delivery che hai misurato. Quali metriche (incluse le DORA: Deployment Frequency, Lead Time, Change Failure Rate, MTTR) hai scelto, perché, e cosa è cambiato?"*

**Monitoring & observability:**
- 🟢 *"Descrivi un'indagine tecnica in cui metriche, log o trace ti hanno dato informazioni diverse. Come hai scelto quale segnale analizzare?"*

**Branching & delivery:**
- 🟢 *"Descrivi il modello di branching di un progetto recente. Come funzionava e quale esigenza del team soddisfaceva?"*
- 🟡 *"Confronta Git Flow e trunk-based development con due contesti concreti in cui sceglieresti diversamente. Quali trade-off valuteresti?"*

<!-- AGENT-FILL: technical_personalized | Genera 5+ domande tecniche neutrali, preferibilmente comportamentali. Terraform / IaC deve essere il primo stack, seguito da AWS / Cloud, Containers, CI/CD, Ansible, Linux / Shell, Git, poi tecnologie specifiche del candidato. Se Terraform non è dichiarato, usa il primo blocco per verificare esperienza IaC equivalente, comprensione concettuale e piano di apprendimento. Ogni domanda con livello e risposta attesa, più un blocco "> **Follow-up di esempio**:". -->

#### Scenario attitudinale — incidente di produzione con vincoli (~10 min)

> **Quando usarlo**: opzionale; utile per valutare il ragionamento sotto pressione e
> la prioritizzazione, soprattutto per profili junior/career-changer.

- 🔴 *"Una modifica trasversale ha rimosso i permessi da una cartella usata da un servizio di produzione containerizzato. Non riesce più a scrivere su una directory mappata sull'host e restituisce 'permission denied'. Puoi usare Docker e leggere i log come tuo utente, ma **non** hai i permessi di root; il team che ha fatto la modifica non è raggiungibile; il restart non ha risolto; la call finisce tra 10 minuti. Come gestisci la situazione, dal primo minuto alla risoluzione? Ragiona ad alta voce."*
  > **Risposta attesa**:
  > - ✅ Metodo e calma: raccoglie i fatti (cosa è cambiato, quando, errore esatto, blast radius), formula e verifica un'ipotesi prima di agire, comunica lo stato.
  > - ✅ Prioritizzazione: separa il ripristino del servizio (ora) da root cause e prevenzione (dopo).
  > - ✅ Ragionamento nei vincoli: cerca un'alternativa nel proprio ambito di accesso (es. ricreare la risorsa invece di modificarla in-place) invece di bloccarsi su "non ho i permessi".
  > - ⚠️ Ritenta il restart senza raccogliere fatti.
  > - 🚫 Va nel panico, agisce a caso in produzione o pretende privilegi come unica via.

---

## Parte 3 — AI assessment (~10 min)

- 🟢 *"Che ruolo hanno avuto finora gli strumenti AI nel tuo lavoro o apprendimento? Se non li hai usati, come hai valutato questa scelta?"*
- 🟡 *"Raccontami un task in cui hai valutato se usare uno strumento AI. Come hai deciso, come hai verificato il risultato e quale impatto hai osservato?"*
- **Setup per round 2**: *"Prima del prossimo colloquio, esplora un assistente AI di coding e tecniche di ottimizzazione dei prompt. La prossima volta ti chiederò cosa hai provato e imparato."*

---

## Esercizi tecnici

> **Workflow a pagina unica**: il prompt completo di ogni esercizio selezionato è
> incorporato qui sotto — l'intero round si conduce da questo file, senza aprire il
> repo esercizi. La tabella è un indice interno: cliccando un titolo si salta al
> prompt incorporato nello stesso documento; le soluzioni non vengono mai
> incorporate qui. Fonte: catalogo esercizi condiviso (vedi
> `../exercise-presets.json` e `../../exercises/`). Ordine: Terraform / IaC →
> AWS / Cloud → Containers → CI/CD → Ansible → Linux / Shell → Git → specifici
> del candidato.

| # | Esercizio | Argomento | Difficoltà | Tempo |
|---|-----------|-----------|------------|-------|
| 1 | [Terraform / IaC — modulo istanza](#exercise-terraform-ec2) | Terraform | Media | 15 min |
| 2 | [Containers — Postgres con volume host](#exercise-docker-postgres) | Containers | Facile | 10 min |
<!-- AGENT-FILL: exercise_table_rows | Aggiungi una riga per ogni esercizio selezionato aggiuntivo (standard + estesi in base allo stack, da exercise-presets.json), ognuno con link alla propria ancora incorporata sotto come #exercise-<id>. Per candidati P1/blended-con-P1/P1-da-verificare aggiungi sempre la riga obbligatoria "python-max-product". -->

<a id="exercise-terraform-ec2"></a>
### Terraform / IaC — modulo istanza

**Prompt**: Crea un modulo Terraform che avvia un'istanza e restituisce il suo private DNS come output (nome modulo `my_instance`).

> **Evidenza attesa**: un blocco `output` funzionante collegato all'attributo della
> risorsa, variabili con default sensati, e una breve spiegazione del perché
> l'output è utile (es. per alimentare un altro modulo). ⚠️ valori hardcoded invece
> di variabili; 🚫 nessun output funzionante.

*(Esercizio inline — scritto direttamente in questo template, nessun file sorgente nel bank da collegare.)*

<a id="exercise-docker-postgres"></a>
### Containers (Docker) — Postgres con volume host

**Prompt**: Avvia un container PostgreSQL con la password in una variabile
d'ambiente e un volume host per la directory dati; verifica che sia in esecuzione.
Spiega vantaggi e rischi dello storage host rispetto a quello del container.

> **Evidenza attesa**: uso corretto di `-e`/`-v` (o equivalente Compose), un passo
> di verifica funzionante (es. `docker exec ... psql`), e un'articolazione chiara
> del trade-off durabilità/portabilità. 🚫 password nell'immagine o verifica
> saltata.

*(Esercizio inline — scritto direttamente in questo template, nessun file sorgente nel bank da collegare.)*

<!-- AGENT-FILL: extra_exercises | Per ogni esercizio aggiuntivo selezionato da exercise-map.json (standard + estesi in base allo stack, da exercise-presets.json): (1) aggiungi una riga alla tabella sopra con link a #exercise-<id>; (2) aggiungi qui una sezione incorporata con `<a id="exercise-<id>"></a>`, un titolo, una riga "**Prompt**:" con il prompt completo copiato dal file del bank (o dal campo "prompt" della voce mappa quando "path" è null) — mai la soluzione; (3) un blocco "> **Evidenza attesa**:"; (4) se la voce mappa ha un "path" reale, un'altra riga: `<a href="file:///<exercises_repo>/<path>" target="_blank" rel="noopener">Apri l'esercizio sorgente dal bank</a>` (risolvi exercises_repo da config/hiring.config.json) — altrimenti scrivi "*(Esercizio inline — nessun file sorgente nel bank.)*". Se una voce mappa non ha né "path" né "prompt" (voce bank incompleta), non inventare un prompt e non modificare il bank: saltala e aggiungi invece un flag di una riga, es. "⚠️ `<id>` non ha un prompt in exercise-map.json — segnalato, non usato in questo round." Per candidati P1, blended con componente P1, o P1 da verificare, includi sempre l'esercizio obbligatorio "python-max-product" (incorpora il suo campo "prompt" testualmente) e marcalo OBBLIGATORIO P1 — non sostituirlo con un altro esercizio Python. Ordina Terraform / IaC per primo. -->

---

## Scorecard (compilare dopo il colloquio)

> Punteggi 1-5. Modello ponderato: Behaviour 40% · Skills 35% · Knowledge 25%.
> Registra i punteggi nel file strutturato con `hiring scorecard init --name "{{CANDIDATE_NAME}}"`,
> compila il JSON ed esegui `hiring scorecard summary --name "{{CANDIDATE_NAME}}"`.

| Dimensione | Punteggio (1-5) | Note |
|-----------|-----------------|------|
| Behaviour | | |
| Skills | | |
| Knowledge | | |
| **Totale ponderato** | | |

**Archetipo di contributo**: `platform_engineering` / `delivery_engineering` / `blended` / `unclear`

**Punti di forza**:
**Preoccupazioni**:
**Raccomandazione provvisoria**:
