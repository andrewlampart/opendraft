## 2.2 Methodology

### 2.2.1 Research Design and Approach

This research employs a qualitative, narrative review methodology to analyze the intersection of technical constraints and cultural adaptation in video game localization. Unlike systematic reviews that adhere to rigid inclusion protocols (e.g., PRISMA) to quantify bibliographic data, a narrative review approach allows for a hermeneutic synthesis of diverse source types—ranging from theoretical monographs to technical case studies—to construct a holistic understanding of the "GILT" (Globalization, Internationalization, Localization, Translation) framework.

The primary objective of this methodology is to synthesize existing empirical data regarding localization workflows in both "AAA" (high-budget) and "Indie" (independent) development environments. By adopting a comparative case study synthesis, this section establishes the analytical framework used to evaluate how different development scales impact translation strategies. The research design is grounded in the foundational theories established by O'Hagan and Mangiron {cite_003} and Bernal-Merino {cite_001}, while integrating contemporary perspectives on neural machine translation (NMT) and deep learning asset generation {cite_010}{cite_019}.

The methodological approach is tripartite:
1. **Theoretical Synthesis:** Establishing definitions for Communicative Translation and Transcreation within the specific context of interactive media.
2. **Comparative Analysis:** Contrasting the rigid, waterfall-style methodologies of AAA production (exemplified by titles like *Black Myth: Wukong*) against the agile, community-driven approaches often seen in indie titles (exemplified by *Stardew Valley*).
3. **Technological Assessment:** Evaluating the impact of emerging tools, such as AI-driven asset generation and automated subtitling, on the traditional translator's role.

### 2.2.2 Data Collection and Source Selection

The literature and data sources analyzed in this study were identified through a comprehensive search of academic databases including Semantic Scholar, IEEE Xplore, and specialized translation studies journals. The selection process prioritized sources that bridge the gap between linguistic theory and software engineering reality.

#### 2.2.2.1 Inclusion Criteria and Search Strategy
Sources were selected based on their relevance to three core thematic pillars: cultural adaptation strategies, technical localization engineering, and player reception. Special attention was paid to recent publications (2020–2025) to ensure the inclusion of current industry practices regarding Games-as-a-Service (GaaS) and AI integration.

Table 3 outlines the categorization of sources used to construct the analytical framework.

| Category | Description | Key Indicators | Representative Sources |
|:--- |:--- |:--- |:--- |
| **Theoretical** | Foundational frameworks | GILT, Skopos, Transcreation | {cite_001}, {cite_003}, {cite_009} |
| **Technical** | Engineering & Tools | NMT, Deep Learning, ISO Standards | {cite_010}, {cite_019}, {cite_045} |
| **Case Study** | Game-specific analysis | *Stardew Valley*, *Black Myth: Wukong* | {cite_006}, {cite_038}, {cite_011} |
| **Sociocultural** | Industry culture & Ethics | Censorship, Gender, Accessibility | {cite_020}, {cite_028}, {cite_008} |

*Table 3: Categorization of Primary and Secondary Sources. Source: Author's categorization based on literature analysis.*

#### 2.2.2.2 Documentation of Industry Practices
Given the proprietary nature of video game development, direct access to source code or internal localization bibles is rarely available in academic research. Therefore, this methodology relies on "grey literature" validation and secondary analysis of detailed case studies. For instance, the technical constraints of text box limitations and variable handling are analyzed through the lens of software testing standards {cite_045} and localization handbooks {cite_035}, rather than direct observation of proprietary engines. This approach mitigates the opacity of the industry—a challenge noted in studies regarding industry protectionism and digital rights management {cite_048}—by triangulating findings across multiple independent reports.

### 2.2.3 Theoretical Framework for Analysis

The analysis of localization strategies is conducted through a dual-lens framework combining **Communicative Translation Theory** and **Multimodal Semiotics**.

#### 2.2.3.1 Communicative Translation in Interactive Media
Traditional translation theory often prioritizes semantic equivalence. However, in video games, the "skopos" (purpose) of the text is primarily to facilitate gameplay and immersion. This research utilizes the Communicative Translation perspective, as applied by Wang {cite_038} in the analysis of *Black Myth: Wukong*. This framework posits that the successful localization of a game is measured not by linguistic accuracy, but by the recreation of the intended "game feel" and narrative impact for the target audience.

The analysis evaluates translation choices based on Newmark’s dichotomy of semantic vs. communicative translation, adapted for the constraints of UI design. For example, when analyzing dialogue in *Stardew Valley* {cite_006}, the methodology examines whether "cultural softening" or "domestication" strategies were employed to make the text acceptable to the target culture, potentially at the expense of the source text's original nuance.

#### 2.2.3.2 Multimodal Semiotics and Audio-Visual Cohesion
Video games are polysemiotic systems where meaning is constructed through text, audio, and visual cues simultaneously. A purely textual analysis is insufficient. Therefore, this methodology incorporates a multimodal analysis framework as described by Bagaskara and Dhanadipa {cite_026} in their study of *Elden Ring*, and Sun et al. {cite_027} regarding audio-visual event localization.

The relationship between these modalities can be formalized to understand the "Translation Load" ($T_L$). If the visual channel ($V$) and audio channel ($A$) provide high context, the reliance on the textual channel ($T$) decreases. Conversely, where visuals are abstract, the text must carry a heavier explanatory load.

The analysis considers the cohesion between these elements:
$$C_{total} = f(T_{sync}, A_{cues}, V_{context})$$

Where $C_{total}$ represents the total semiotic cohesion perceived by the player. This formulation allows for the evaluation of "ludonarrative dissonance" caused by poor localization—for instance, when a translated subtitle contradicts a visual cue or an audio prompt, a phenomenon investigated in studies on audio description and accessibility {cite_008}.

### 2.2.4 Comparative Case Study Framework: AAA vs. Indie

To address the research gap regarding the "Indie vs. AAA" divide identified in the literature review, this methodology establishes a comparative matrix. This matrix distinguishes between the resource-rich, highly stratified workflows of AAA studios and the resource-constrained, often community-reliant workflows of indie developers.

#### 2.2.4.1 Defining the Variables
The comparison is not merely financial but methodological. AAA localization is characterized by the simultaneous shipment of multiple languages (Sim-ship), requiring robust "Internationalization" (i18n) phases integrated into the code structure early in development {cite_035}. In contrast, indie localization often occurs post-release, sometimes utilizing fan translations or crowdsourcing, which introduces unique quality control and consistency challenges.

Table 4 defines the specific variables used to analyze the case studies in the subsequent Analysis section.

| Variable | AAA Characteristics (e.g., *Black Myth*) | Indie Characteristics (e.g., *Stardew Valley*) | Implications for Analysis |
|:--- |:--- |:--- |:--- |
| **Workflow** | Integrated, Simultaneous | Post-release, Sequential | Impact on context availability |
| **Technology** | Proprietary engines, AI integration | Unity/Godot, Manual spreadsheets | Technical constraint rigidity |
| **Cultural Strategy** | Market-driven, "Culturally Odorless" | Auteur-driven, Niche appeal | Domestication vs. Foreignization |
| **QA Process** | LQA teams, Automated testing | Community feedback, Beta branches | Error frequency and type |

*Table 4: Comparative Variables for AAA vs. Indie Localization Analysis. Source: Adapted from {cite_003} and {cite_006}.*

#### 2.2.4.2 The Role of Technical Constraints
A critical component of this methodology is the isolation of **technical constraints** as a determinant of translation strategy. Literature indicates that translators often modify text not for cultural reasons, but to fit strict character limits or memory buffers {cite_002}. The analysis distinguishes between:
1. **Hard Constraints:** Fixed byte limits, UI pixel width, non-resizable text boxes.
2. **Soft Constraints:** Reading speed guidelines for subtitles, synchrony with lip movements (labial sync).

By applying the definitions from Corbolante and Irmler {cite_035} regarding software terminology and localization, the analysis seeks to identify instances where technical limitations forced a "simplification" strategy, distinguishing this from stylistic choices.

### 2.2.5 Analytical Categories for Cultural Adaptation

Beyond technical constraints, the methodology examines the cultural dimensions of localization using the Domestication and Foreignization spectrum. This approach draws on the work of Cao {cite_017} and Dong and Mangiron {cite_029} regarding the adaptation of games for specific markets, such as China.

#### 2.2.5.1 Taxonomy of Cultural Realia
To systematically analyze how cultural elements are handled, this research utilizes a taxonomy of "Cultural Realia" based on Moreno García’s work {cite_011}. The analysis categorizes in-game assets into:
* **Ecological Realia:** Flora, fauna, and geographical features specific to the source culture.
* **Material Realia:** Food, clothing, and architecture.
* **Social Realia:** Legal systems, religious practices, and historical references.

For each instance of realia identified in the case studies (e.g., Chinese mythological figures in *Black Myth: Wukong* or farming festivals in *Stardew Valley*), the translation strategy is classified according to the following strategies:
1. **Preservation:** Keeping the term in the source language (Foreignization).
2. **Literal Translation:** Calque.
3. **Cultural Equivalent:** Replacing the item with a target-culture equivalent (Domestication).
4. **Omission:** Removing the reference entirely.

This classification allows for a quantitative comparison of strategy frequency between the selected titles, providing empirical evidence for the "cultural softening" hypothesis proposed by Wang {cite_006}.

#### 2.2.5.2 Analyzing Censorship and Regulation
A subset of cultural adaptation involves regulatory compliance and censorship. Drawing on Bates {cite_028} regarding censorship mechanisms and Roomberg {cite_036} regarding industry regulation, the methodology includes a review of changes mandated by regional laws (e.g. Prohibition of skeletons or gambling mechanics). This is particularly relevant for the "Journey to the East" context described by Dong and Mangiron {cite_029}, where Western games must undergo significant modification to enter the Chinese market. The analysis treats these regulatory changes as "Mandated Localization," distinct from "Creative Localization."

### 2.2.6 Evaluation of Technological Integration (AI and NMT)

The final pillar of the methodology addresses the rapid integration of Artificial Intelligence in the localization pipeline. This section moves beyond traditional GILT frameworks to incorporate recent findings on Deep Learning and Neural Machine Translation (NMT).

#### 2.2.6.1 Assessing Automated Workflows
The analysis utilizes the framework proposed by Ribeiro et al. {cite_010} for evaluating deep learning assets and Aytaş {cite_019} for multimodal NMT. The methodology involves a theoretical assessment of where AI tools are currently deployed in the localization chain:
* **Pre-production:** AI-generated placeholder text and synthetic voice-overs.
* **Production:** NMT drafts for post-editing (PEMT).
* **Post-production:** Automated LQA (Language Quality Assurance) checks.

The study contrasts the efficiency gains reported in technical literature {cite_045} with the quality concerns raised in translation studies. Specifically, it examines the "context blindness" of NMT engines—their inability to distinguish between homonyms based on game state—and how human translators mitigate this.

#### 2.2.6.2 Accessibility as a Localization Vector
Modern localization increasingly overlaps with accessibility. The methodology includes **Audio Description (AD)** and **Subtitling for the Deaf and Hard of Hearing (SDH)** as forms of intersemiotic translation. Following Larreina and Mangiron {cite_008} and Westin {cite_049}, the analysis evaluates how accessibility features are localized. For example, does the localized version of a game retain the detailed audio cues required for visually impaired players? This expands the definition of "localization" to include the translation of sensory experience, not just text.

### 2.2.7 Methodological Limitations

While this narrative review and comparative framework provide a robust structure for analysis, several limitations inherent to the research design must be acknowledged.

#### 2.2.7.1 Lack of Access to Source Code
A primary limitation in video game research is the "Black Box" nature of proprietary software. As noted by Pachali {cite_048}, developers aggressively protect their intellectual property. Consequently, this study cannot verify the exact code-level implementation of localization strings (e.g. Whether a string is hard-coded or called from an external database) unless explicitly documented in post-mortem reports or technical papers. The analysis relies on the *observable output* (the game on screen) rather than the *input mechanism* (the code).

#### 2.2.7.2 Bias in Source Availability
The selection of case studies and supporting literature reflects a bias toward major linguistic pairs, specifically English-Chinese and English-European languages. Sources such as Wang {cite_006}, {cite_038} and Dong and Mangiron {cite_029} provide extensive data on the Chinese market, while other regions (e.g., Arabic, Hindi) are underrepresented in the available citation database. This geographic limitation may skew the understanding of "universal" localization challenges.

#### 2.2.7.3 The "Gamer" Variable
Finally, analyzing player reception through bibliometrics and review aggregation, as discussed by Meho {cite_043}, presents challenges in sentiment analysis. Player reviews are often polarized or focus on gameplay mechanics rather than translation quality. Disentangling complaints about "bugs" from complaints about "localization errors" requires careful qualitative coding. Furthermore, the demographic profile of players leaving reviews may not represent the broader player base, introducing a selection bias in the reception analysis.

### 2.2.8 Synthesis of Analytical Approach

In summary, the methodology adopted for this thesis is a **multiperspective comparative analysis**. It triangulates data from theoretical models (GILT), technical specifications (ISO standards/Platform guidelines), and cultural case studies (AAA vs. Indie).

The analytical process proceeds in three stages:
1. **Deconstruction:** Breaking down the selected games into their constituent localizable assets (text, audio, graphics).
2. **Categorization:** Classifying the adaptation strategies applied to these assets using the taxonomy defined in Table 4 (Preservation, Substitution, Omission).
3. **Correlation:** Mapping these strategies against the identified constraints (Technical limits, Cultural taboos, Budgetary restrictions) to determine causality.

This structured approach allows the research to move beyond anecdotal observation of "funny translation errors" to a rigorous examination of the systemic forces—technological, economic, and cultural—that shape the final localized product. By integrating the communicative perspective {cite_038} with the technical realities of asset generation {cite_010}, the methodology is equipped to address the complex, interdisciplinary nature of modern video game localization.

### 2.2.9 Ethical Considerations in Game Localization Research

Although this study does not involve human participants in an experimental setting, ethical considerations regarding the representation of developer labor and player culture are pertinent. Jacobs-Johnson {cite_020} highlights the gendered and often precarious nature of production culture in the gaming industry. In analyzing localization failures or "crunched" workflows, this research maintains an ethical stance that avoids assigning individual blame to translators, recognizing instead the structural pressures of the industry. Furthermore, when discussing therapeutic or serious games, as explored by Jeanmaire and Kim {cite_021}, the analysis respects the medical and vulnerable context of the target audience, ensuring that critiques of localization do not undermine the therapeutic intent of the software.

The following sections (Analysis and Results) will apply this methodological framework to the selected case studies, presenting a detailed examination of how the tension between technical rigidity and cultural fluidity is negotiated in practice.