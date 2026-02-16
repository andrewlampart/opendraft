## 2.1 Literature Review

The academic study of video game localization has evolved significantly over the past two decades, transitioning from a peripheral interest within Translation Studies to a distinct, interdisciplinary field that intersects with ludology, software engineering, and cultural studies. As the video game industry has expanded globally, surpassing the revenue of the film and music industries combined, the necessity for sophisticated localization strategies has become paramount. This literature review synthesizes existing research to establish a theoretical framework for analyzing the localization process. It examines the shift from linguistic equivalence to "transcreation," the technological constraints inherent to the medium, the cultural adaptation of narrative and character assets, and the emerging role of artificial intelligence in automating localization workflows.

### 2.1.1 Theoretical Frameworks and Definitions

To understand the complexities of game localization, it is necessary first to define the theoretical boundaries that distinguish it from traditional forms of translation, such as literary or technical translation. The literature consistently points to the insufficiency of traditional equivalence-based theories when applied to interactive media.

#### 2.1.1.1 From Translation to Transcreation
The foundational concept in modern game localization scholarship is the shift from "translation" to "transcreation." O'Hagan and Mangiron {cite_003} provide the seminal definition of this paradigm, arguing that game localization must prioritize "playability" and the "fun factor" over semantic accuracy. In their comprehensive monograph, they establish that the interactive nature of video games requires localizers to act as co-creators who adapt content to evoke the same emotional response in the target player as experienced by the source player, even if this requires significant deviation from the source text.

This approach is further supported by Bernal-Merino {cite_001}, who emphasizes that the "skopos" (purpose) of the game—entertainment—dictates the translation strategy. He argues that a literal translation that preserves meaning but disrupts the user interface (UI) or fails to convey the game's mechanics effectively renders the product defective. Consequently, transcreation involves rewriting dialogue, renaming characters, and even altering narrative arcs to suit the target culture's expectations and the game's mechanical constraints.

#### 2.1.1.2 The GILT Model
The industry standard for conceptualizing these processes is the GILT framework (Globalization, Internationalization, Localization, Translation). O'Hagan and Mangiron {cite_003} and Mejías-Climent {cite_009} describe this hierarchy as follows:

1. **Globalization:** The business decisions regarding which markets to enter.
2. **Internationalization (i18n):** The technical preparation of the code to handle different languages (e.g. Character encoding, variable UI expansion).
3. **Localization (l10n):** The adaptation of linguistic and cultural assets.
4. **Translation (t9n):** The specific rendering of text from one language to another.

Mejías-Climent {cite_030} expands on this by analyzing the history of these processes, noting that early localization was often an afterthought, leading to "hard-coded" text that was impossible to translate without rewriting the game engine. Modern frameworks, however, integrate internationalization at the pre-production stage, allowing for more seamless localization.

#### 2.1.1.3 Communicative Translation Theory
Recent scholarship has applied Newmark’s Communicative Translation Theory to video games, particularly in the context of high-fidelity narratives. Wang {cite_038} applies this lens to the localization of *Black Myth: Wukong*, arguing that for games deeply rooted in specific mythologies, the translator's primary goal is communicative efficacy—ensuring the target audience understands the cultural function of the text—rather than semantic fidelity. This aligns with the broader move toward "domestication" or "foreignization" strategies discussed by Cao {cite_017}, who compares these approaches in literary translation. In the context of games, communicative translation ensures that the "gameplay loop" is not interrupted by linguistic confusion.

### 2.1.2 Cultural Adaptation and Asset Management

The localization of cultural "realia"—items, names, and concepts specific to a culture—presents unique challenges in video games due to the multimodal nature of the medium. Unlike a novel, where a footnote can explain a cultural term, a video game must convey information instantaneously to avoid breaking immersion.

#### 2.1.2.1 Adaptation of Character and Narrative
Character development relies heavily on culturally coded dialogue and visual markers. Wang {cite_006} investigates this through the lens of *Stardew Valley*, analyzing how the English character dialogue was translated into Chinese. The study finds that successful character localization requires reconstructing the "personality" of the character using target-culture sociolinguistic markers. For instance, a character speaking in a rural dialect in English might be mapped to a specific regional dialect in Chinese to preserve the "rustic" characterization, a strategy that goes beyond lexical translation to encompass sociolinguistic equivalence.

Similarly, Moreno García {cite_011} examines the localization of *Arena of Valor*, a Multiplayer Online Battle Arena (MOBA) game. This genre relies heavily on distinct character archetypes drawn from folklore and history. The study highlights how "cultural realia" are adapted or entirely replaced to resonate with international players. In some cases, characters based on obscure Chinese historical figures were replaced with Western superheroes (e.g., Batman) for the European release, a radical form of transcreation designed to lower the cultural barrier to entry.

#### 2.1.2.2 Visual and Semiotic Analysis
Video games convey meaning through a complex interplay of visual, auditory, and textual signs. Bagaskara and Dhanadipa {cite_026} conduct a semiotic analysis of boss cutscenes in *Elden Ring*, demonstrating how visual signs (costume, lighting, gesture) serve as narrative devices that function independently of the text. This implies that localization is not merely about translating subtitles but ensuring that the translated text does not contradict the immutable visual information on screen.

Furthermore, Sun et al. {cite_027} discuss "Audio-Visual Event Localization" (AVEL), noting the robust complementary correlation between audio and visual signals. While their work focuses on technical detection, the implication for localization is clear: the semantic load is shared between what is seen and what is heard. If a localization changes the dialogue (audio/text) significantly, it risks creating dissonance with the visual track, a phenomenon known as "ludonarrative dissonance."

#### 2.1.2.3 Cross-Cultural Market Strategies
The flow of cultural products is no longer unidirectional (West to East). Dong and Mangiron {cite_029} analyze the "Journey to the East," focusing on the adaptation of Western games for the Chinese market. They identify strict regulatory requirements and distinct gamer preferences as drivers for localization. Conversely, the rise of the Turkish game industry, as documented by Üyesi et al. {cite_014}, and the global success of Chinese AAA titles like *Black Myth: Wukong* {cite_038}, illustrate a "Journey to the West" where non-Western cultural assets must be adapted for global consumption.

Table 1 summarizes the primary cultural adaptation strategies identified in the literature.

| Strategy | Definition | Key Application | Theoretical Basis |
|:--- |:--- |:--- |:--- |
| **Transcreation** | Creative rewriting to preserve "fun factor" | Humor, puns, culturally specific quests | {cite_003}, {cite_011} |
| **Domestication** | Replacing source culture elements with target culture equivalents | Character names, food items, holidays | {cite_017}, {cite_006} |
| **Foreignization** | Retaining source culture elements to preserve "exoticism" | Historical titles, specific mythologies (*Wukong*) | {cite_017}, {cite_038} |
| **Neutralization** | Removing cultural markers to create a "generic" international version | UI icons, color schemes, taboo topics | {cite_029} |
| **Visual Adaptation** | Modifying graphical assets to meet legal or cultural norms | Skeletons in Chinese releases, blood color | {cite_010}, {cite_029} |

*Table 1: Taxonomy of Cultural Adaptation Strategies in Video Game Localization. Source: Adapted from {cite_003}, {cite_017}, and {cite_029}.*

The choice between these strategies is often dictated by the genre. Narrative-heavy games (RPGs) may favor foreignization to immerse players in a specific world, while casual mobile games often employ domestication or neutralization to maximize broad appeal.

### 2.1.3 Technological Constraints and Innovations

Unlike other forms of audiovisual translation, game localization is fundamentally constrained by software engineering. The literature identifies the interplay between code and text as a defining characteristic of the field.

#### 2.1.3.1 Internationalization and Variable Management
Corbolante and Irmler {cite_035} discuss software terminology and localization, emphasizing the technical rigidity of string management. Text in games is often stored in spreadsheets or databases where context is stripped away. A translator might see the word "Turn" and not know if it refers to a "turn" in a car, a "turn" in a strategy game, or the act of "turning" around. O'Hagan and Mangiron {cite_003} highlight that training translators to deal with these "context-deprived" environments is crucial.

Furthermore, Westin {cite_049} surveys engine-independent solutions for accessibility, which has implications for localization. The way an engine handles text display (fonts, character limits, text wrapping) determines the translator's constraints. If a dialogue box allows only 50 characters, the German translation (which is typically 30% longer than English) must be truncated or rewritten, regardless of semantic accuracy.

#### 2.1.3.2 The Rise of AI and Neural Machine Translation
The integration of Artificial Intelligence (AI) and Machine Learning (ML) is reshaping the localization workflow. Aytaş {cite_019} investigates the impact of integrating visual and auditory modalities into Neural Machine Translation (NMT). Traditional NMT models often fail in creative domains because they lack context. However, Aytaş demonstrates that multimodal NMT, which "sees" the game asset associated with the text, significantly improves translation quality by resolving ambiguities.

Ribeiro et al. {cite_010} provide a systematic review of deep learning for asset generation. They note that Deep Learning can now automate the creation of graphical content, including user interfaces and typographical elements. This has profound implications for "deep localization," where AI could theoretically generate localized textures (e.g. Changing a "Stop" sign in the game world to "Arrêt" for the French version) automatically, a process that was previously too labor-intensive for most productions.

#### 2.1.3.3 Dubbing and Audio Technologies
Audio localization, or dubbing, adds another layer of complexity. Mejías-Climent {cite_025} analyzes dubbing through specific game situations, noting that synchronization in games is harder than in film because the timing can be variable (dynamic) based on player input. Saralegi et al. {cite_044} discuss the development of automatic multilingual subtitling and dubbing systems, such as "MULTILINGTOOL." These tools aim to streamline the synchronization process, though challenges remain in preserving the emotional nuance of voice acting when using automated solutions.

### 2.1.4 Pedagogical Perspectives and Industry Training

Given the specialized nature of game localization, the literature emphasizes the need for specific pedagogical approaches. General translation training is insufficient for the demands of the industry.

#### 2.1.4.1 Specialized Competencies
Bernal-Merino {cite_001} was among the first to outline a curriculum for game localization, identifying the need for "technological competence" alongside linguistic skill. Translators must understand variables, tags, and basic coding syntax. Morais {cite_002} reviews Bernal-Merino's work, reinforcing the idea that localization education must bridge the gap between the commercial and translational aspects of the industry.

#### 2.1.4.2 Blended Learning Resources
Merten {cite_016} advocates for creating "blended resources" for translator training, combining traditional translation theory with practical software testing. This aligns with the findings of Ali and Yue {cite_045}, who formalize software testing standards. In the context of localization, "Linguistic Quality Assurance" (LQA) is a form of software testing. Translators must be trained not just to translate, but to "bug test" language within the build, identifying text overlaps, missing glyphs, and coding errors.

### 2.1.5 Accessibility and Inclusion in Localization

A rapidly expanding sub-field within localization research is accessibility. Localization is increasingly viewed not just as language transfer, but as a means of making games accessible to players with different abilities.

#### 2.1.5.1 Audio Description and Visual Impairment
Larreina and Mangiron {cite_008} argue that accessibility features like Audio Description (AD) are a form of intersemiotic translation. Since 2020, game accessibility has gained traction, with features for players with visual disabilities becoming more common. The localization of these features—translating the audio description tracks or the screen reader metadata—is a new frontier. A game that is accessible in English but fails to localize its accessibility options into Spanish effectively excludes disabled players in that market.

#### 2.1.5.2 Gender and Representation
Jacobs-Johnson {cite_020} analyzes gender representation in game production culture. This is relevant to localization because the demographics of the localization team often influence the output. If the localization team lacks diversity, gendered language or inclusive terminology may be mishandled. Jeanmaire and Kim {cite_021} explore this in a therapeutic context, discussing the translation of games for children with asthma. They note that translating for vulnerable populations requires a balance between "localization" and "medical vulgarisation" (simplification), ensuring that medical terms are accurate yet understandable across cultures.

### 2.1.6 Empirical Studies on Specific Genres

The literature reveals that localization strategies are highly genre-dependent.

#### 2.1.6.1 Serious and Therapeutic Games
Ohori et al. {cite_039} discuss the "Reorganizing Public Facilities Game," a serious game used for urban planning. Here, the priority is not entertainment but clarity and educational value. Similarly, Jeanmaire and Kim {cite_021} highlight that in therapeutic games, the "fun factor" is secondary to clinical adherence. Localization errors in these contexts can have real-world health or policy consequences, demanding a much higher degree of semantic accuracy than entertainment titles.

#### 2.1.6.2 Massive Multiplayer and Live Service Games
The shift to "Games as a Service" (GaaS) has introduced the need for continuous localization. In the case of *Arena of Valor* {cite_011}, the game is constantly updated with new heroes and items. This requires a "sim-ship" (simultaneous shipment) model, where localization occurs in parallel with development. This contrasts with the older "post-gold" model described in earlier texts like O'Hagan and Mangiron {cite_003}, where localization began after the game was finished.

### 2.1.7 Legal and Ethical Considerations

Finally, the literature touches upon the legal and ethical dimensions of the global game trade. Roomberg {cite_036} discusses the video game industry's money laundering problems and the legal responsibilities of publishers. While primarily legal research, this impacts localization regarding terminology for in-game currencies and "loot boxes," which face different legal definitions in countries like Belgium versus the United States. Localization teams must be aware of these legal nuances to avoid non-compliance. Additionally, Bates {cite_028} provides historical context on censorship, which remains relevant as localizers must navigate state regulations (e.g., China's restrictions on depictions of time travel or skeletons) that necessitate content modification.

### 2.1.8 Synthesis and Research Gaps

The review of the existing literature reveals a robust theoretical foundation established by O'Hagan, Mangiron, and Bernal-Merino, which successfully legitimizes game localization as a complex form of transcreation. However, several gaps remain that this study aims to address.

**1. The Gap in AI-Human Collaboration Models:**
While recent papers like Aytaş {cite_019} and Ribeiro et al. {cite_010} discuss the technical capabilities of AI, there is a lack of empirical research on the *workflow integration* of these tools. How do human localizers perceive and edit AI-generated assets in high-stakes AAA productions compared to indie titles?

**2. The "Indie" vs. "AAA" Divide:**
Much of the literature focuses on major commercial titles or generic theoretical models. There is less comparative analysis on how independent developers, who lack the resources for comprehensive GILT workflows, manage localization. Wang's study on *Stardew Valley* {cite_006} is a step in this direction, but broader comparative studies are needed.

**3. Longitudinal Reception Studies:**
While strategies are well-documented, player reception remains under-researched. Meho {cite_043} discusses bibliometric anomalies and metrics, but there is a lack of quantitative data connecting specific localization strategies (e.g. Domestication) to player review scores or sales performance in specific regions.

Table 2 highlights the evolution of research focus in the field, demonstrating the trajectory from definition to technological integration.

| Era | Primary Focus | Key Scholars | Methodological Trend |
|:--- |:--- |:--- |:--- |
| **Foundational (2000-2013)** | Defining the field, GILT framework, Transcreation | {cite_003}, {cite_001} | Case studies, Theoretical monographs |
| **Expansion (2014-2019)** | Cultural adaptation, Training, Mobile gaming | {cite_029}, {cite_002} | Comparative analysis, Pedagogical review |
| **Technological (2020-Present)** | AI/NMT integration, Accessibility, Deep Learning | {cite_010}, {cite_019}, {cite_008} | Systematic reviews, Experimental design |

*Table 2: Evolution of Research Themes in Video Game Localization. Source: Author's synthesis of literature.*

By addressing these gaps, specifically the intersection of cultural adaptation strategies and emerging technical constraints in the modern "Live Service" era, this research contributes to the next phase of game localization scholarship. The following sections will outline the methodology used to investigate these dynamics in the selected case studies.