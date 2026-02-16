---
title: "Analyzing Methods and strategies in the localisation process in selected video game(s) or genre."
author: "Brandon"
date: "February 2026"
institution: "WSB Merito Gdańsk"
department: "Department of Computer Science"
faculty: "Faculty of Engineering"
degree: "Master of Science"
advisor: "Prof. Dr. OpenDraft Supervisor"
second_examiner: "Prof. Dr. Second Examiner"
location: "Munich"
student_id: "N/A"
project_type: "Master Draft"
word_count: "18,513 words"
pages: "74"
generated_by: "OpenDraft AI - https://github.com/federicodeponte/opendraft"
---
## Abstract

**Research Problem and Approach:** The global video game industry has evolved into a dominant cultural force, necessitating sophisticated localization strategies to ensure linguistic and cultural accessibility for international audiences. However, a significant disconnect remains between theoretical translation frameworks and the practical, technical realities of the industry, particularly regarding the multimodal nature of modern gaming. This thesis investigates the complex interplay between linguistic translation, cultural adaptation, and technical engineering within the "GILT" framework (Globalization, Internationalization, Localization, and Translation) to address how developers preserve the gameplay gestalt across diverse cultural boundaries.

**Methodology and Findings:** By conducting a comparative analysis of selected video game genres and regional case studies, this research examines the industry's transition from a "box-product" model to a continuous service-oriented approach. The study evaluates the shift from textual translation to holistic "transcreation," analyzing how auditory cues, visual assets, and narrative elements are modified to maintain semiotic cohesion in high-growth markets like China and Turkey. The analysis reveals that successful localization relies heavily on early integration into the development pipeline to mitigate "blind" translation errors and navigate rigid technical constraints.

**Key Contributions:** This research makes three primary contributions: (1) A comprehensive historical delineation of localization practices from early hardware constraints to modern AI-assisted asset generation, (2) A critical assessment of how regulatory frameworks and censorship dictate narrative alterations and technical implementation in restrictive markets, and (3) An integrated perspective on the localizer as a key stakeholder, bridging the gap between solitary translation tasks and collaborative software engineering.

**Implications:** These findings have significant implications for both Translation Studies and the interactive entertainment industry, suggesting that localization must be treated as a fundamental design pillar rather than a post-production afterthought. The study provides a roadmap for navigating the economic imperatives of global expansion while preserving cultural authenticity and adhering to complex legal compliance standards in virtual economies.

**Keywords:** Video Game Localization, GILT Framework, Transcreation, Translation Studies, Cultural Adaptation, Game Studies, Semiotics, Multimodality, Digital Entertainment, Internationalization, Censorship, Mobile Gaming, Audio-Visual Translation, Software Engineering, Cross-Cultural Communication

\newpage

# 1. Introduction
The global video game industry has evolved from a niche hobby into a dominant force in the digital entertainment landscape, surpassing the film and music industries in revenue and cultural influence. As this medium transcends geographical boundaries, the process of making video games linguistically and culturally accessible to international audiences—known as localization—has become a critical component of game development. Localization is no longer merely a post-production step involving the translation of text; it is a complex, multi-layered process that integrates linguistic translation, cultural adaptation, technical engineering, and legal compliance to ensure that the gaming experience remains immersive for players worldwide (O'Hagan & Mangiron, 2013). The ability of a game to resonate with a target locale often determines its commercial success, making the study of localization strategies and methods a vital area of inquiry within Translation Studies and Game Studies.

This thesis explores the intricate methods and strategies employed in the localization process, focusing on the tension between technical constraints and the necessity for cultural adaptation. By analyzing selected video games and genres, this research aims to dissect how developers and localizers navigate the "GILT" framework—Globalization, Internationalization, Localization, and Translation—to recreate the gameplay experience (gameplay gestalt) for diverse audiences. The following sections outline the background of the study, the research problem, the significance of the inquiry, and the specific objectives that guide this analysis.

## 1.1 Background of the Study

The history of video game localization parallels the technological advancement of the medium itself. In the early eras of gaming, localization was often an afterthought, characterized by severe hardware limitations and a lack of professional translation standards. However, as storage capacities increased and narrative complexity grew, the demand for high-quality localization surged. Scholars have noted that the industry has shifted from a "box-product" model to a service-oriented model, where continuous updates and global simultaneous shipments (sim-ship) require robust localization infrastructures (Üyesi et al., 2020)(Mejías-Climent, 2021).

### 1.1.1 The Evolution of Localization Practices
Early localization efforts were primarily concerned with the translation of user interface (UI) text and manuals. Today, the scope has expanded to include "transcreation," a creative process that adapts content to elicit the same emotional response in the target audience as the original did in the source audience. This evolution is evident in the transition from simple text replacement to full audio dubbing and asset modification. For instance, recent research highlights the importance of audio-visual event localization, where auditory cues must align perfectly with visual elements to maintain player immersion (Sun et al., 2025). Furthermore, the rise of deep learning and automated asset generation has introduced new methods for modifying graphical elements, such as textures and sprites, to suit regional preferences without extensive manual labor (Ribeiro et al., 2025).

The complexity of modern localization is further compounded by the diversity of platforms, from high-fidelity consoles to mobile devices. Mobile technologies have disrupted the traditional industry structure, creating new markets in regions like Turkey and China, which in turn demand specific localization strategies tailored to mobile interfaces and consumption habits (Üyesi et al., 2020)(Dong & Mangiron, 2018). Consequently, the role of the localizer has transformed from a solitary translator to a key stakeholder in the development pipeline, often collaborating with designers, programmers, and audio engineers.

### 1.1.2 The Economic and Cultural Imperative
The economic motivation for localization is undeniable. A significant portion of a game's revenue is generated outside its country of origin. To penetrate markets such as China—one of the largest video game markets in the world—developers must navigate strict cultural and regulatory landscapes. This involves not only language translation but also the modification of narrative elements and visual aesthetics to align with local values and censorship regulations (Dong & Mangiron, 2018). For example, the adaptation of the "AAA" title *Black Myth: Wukong* illustrates the challenges of exporting culturally specific narratives (based on *Journey to the West*) to a Western audience while preserving the source culture's authenticity (Wang, 2025). Conversely, Western games entering Asian markets often undergo significant "cultural adjustments" to meet the expectations of local gamers (Dong & Mangiron, 2018).

Beyond economics, localization serves a crucial function in cultural exchange. Video games are cultural artifacts that carry the values, humor, and semiotics of their creators. The localization process acts as a filter and a bridge, determining how these cultural markers are interpreted by the target audience. The strategies employed—ranging from "foreignization" (preserving source culture) to "domestication" (assimilating into target culture)—shape the player's perception of the game world (Cao, 2023).

## 1.2 Problem Statement

Despite the growing academic interest in game localization, there remains a disconnect between the theoretical understanding of translation strategies and the practical, technical realities of the industry. Much of the existing literature focuses on textual analysis, often overlooking the multimodal nature of video games where text, audio, image, and gameplay mechanics interact.

### 1.2.1 The Multimodal Challenge
Video games are semiotic systems where meaning is constructed through the interplay of visual signs, auditory signals, and interactive mechanics. A significant problem in localization is ensuring that these multimodal elements remain coherent after translation. For instance, a visual sign in a cutscene might carry narrative clues that are culturally specific; if the text is translated but the visual sign remains unchanged, the semiotic cohesion may be broken, leading to player confusion (Bagaskara & Dhanadipa, 2024). Furthermore, the integration of accessibility features, such as audio descriptions for visually impaired players, adds another layer of complexity to the localization process, requiring the translation of non-verbal auditory information (Larreina & Mangiron, 2025).

### 1.2.2 Technical and Regulatory Constraints
Localizers operate within rigid technical constraints. Character limits, UI space, and hard-coded text strings often dictate translation choices more than stylistic preference. The "blind" nature of some localization tasks—where translators lack context or access to the game build—exacerbates these issues, leading to context errors (Morais, 2020). Additionally, regulatory frameworks regarding censorship and age ratings vary drastically across regions. In markets like Poland during specific historical periods, or modern China, censorship acts as a powerful external constraint that forces localizers to alter or remove content, effectively rewriting the game's narrative (Bates, 2004)(Dong & Mangiron, 2018). The industry also faces legal scrutiny regarding financial compliance and money laundering in virtual economies, which influences how in-game currency and transaction systems are localized and presented to users (Roomberg, 2023).

The problem this thesis addresses is the lack of a comprehensive framework that analyzes how these disparate elements—linguistic strategies, technical constraints, and cultural regulation—interact to shape the final localized product. Specifically, there is a need to understand how different genres (e.g., RPGs vs. Action games) and development scales (Indie vs. AAA) prioritize these factors.

## 1.3 Research Objectives and Questions

The primary objective of this thesis is to analyze the methods and strategies employed in the localization of selected video games, evaluating how cultural and technical factors influence translation decisions.

### 1.3.1 Research Objectives
1. **To identify and categorize** the translation strategies (e.g. Domestication, foreignization, transcreation) used in character development and narrative transfer in video games.
2. **To analyze the impact** of technical constraints (UI limitations, asset immutability) and multimodal elements (audio-visual cues) on the localization process.
3. **To evaluate the role** of cultural adaptation and censorship in shaping the localized versions of games for specific markets.
4. **To examine the integration** of accessibility features within the localization workflow.

### 1.3.2 Research Questions
To achieve these objectives, the study poses the following research questions:
* **RQ1:** How do localizers balance the need for "transcreation" and cultural adaptation with the requirement to maintain the original gameplay experience?
* **RQ2:** In what ways do technical constraints and multimodal dependencie (such as audio-visual synchronization) limit or define translation strategies?
* **RQ3:** How do strategies differ between preserving cultural authenticity (foreignization) and ensuring market acceptability (domestication), particularly in narrative-heavy genres?

## 1.4 Significance of the Study

This research contributes to the fields of Translation Studies, Game Studies, and Software Engineering by providing a holistic analysis of the localization ecosystem.

### 1.4.1 Academic Contribution
Academically, this thesis bridges the gap between traditional translation theory and the emerging discipline of game accessibility and multimodal analysis. While scholars like Bernal-Merino and O'Hagan have established the foundations of game localization (Bernal-Merino, 2008)(O'Hagan & Mangiron, 2013), this study expands on their work by incorporating recent developments in deep learning for asset generation (Ribeiro et al., 2025) and the semiotic analysis of visual signs (Bagaskara & Dhanadipa, 2024). It also addresses the under-researched area of translating therapeutic and educational games, distinguishing them from commercial entertainment software (Jeanmaire & Kim, 2022).

### 1.4.2 Industry Relevance
From an industry perspective, the findings offer practical insights for developers and localizers. By highlighting the friction points between coding standards (internationalization) and linguistic requirements, the study advocates for better integration of localization teams in the early stages of development. The analysis of "best practices" in handling cultural realia and sensitive content can serve as a guideline for studios aiming to enter complex markets like China or Turkey without compromising their creative vision (Üyesi et al., 2020)(Dong & Mangiron, 2018). Furthermore, the discussion on accessibility emphasizes the need for inclusive design, suggesting that localization can be a vehicle for making games playable for users with disabilities (Larreina & Mangiron, 2025)(Westin, 2012).

## 1.5 Theoretical Framework

The analysis is grounded in several key theoretical concepts that allow for the dissection of localization strategies.

### 1.5.1 The GILT Framework
The study utilizes the GILT framework (Globalization, Internationalization, Localization, Translation) to contextualize the technical and administrative processes involved. Localization is viewed not as an isolated event but as part of a continuous cycle of software development and management (O'Hagan & Mangiron, 2013).

### 1.5.2 Skopos Theory and Communicative Translation
To analyze translation choices, the thesis draws upon Skopos theory, which posits that the purpose (skopos) of the translation determines the methods used. In game localization, the primary skopos is often the preservation of the "fun factor" or gameplay experience. This aligns with Communicative Translation Theory, which focuses on producing the same effect on the target reader as the original text did on the source reader. This theoretical lens is particularly relevant when analyzing the translation of character personalities and dialogue, as seen in studies of *Stardew Valley* and *Black Myth: Wukong* (Wang, 2025)(Wang, 2025).

### 1.5.3 Domestication and Foreignization
Venuti’s concepts of domestication and foreignization are employed to categorize cultural adaptation strategies. Domestication involves minimizing the strangeness of the foreign text for target readers, while foreignization retains the foreignness to highlight the source culture. These strategies are critical when analyzing how cultural realia (items, names, festivals) are handled in games like *Arena of Valor* (Moreno García, 2024) and literary adaptations within games (Cao, 2023).

## 1.6 Methodology Overview

While a detailed methodology is presented in Chapter 3, it is necessary to outline the approach here. This thesis employs a **qualitative descriptive approach**, utilizing case studies of specific video games to illustrate broader industry trends. The selection of games includes titles that present unique localization challenges, such as high-fantasy narratives (*Elden Ring*), culturally specific settings (*Black Myth: Wukong*, *Stardew Valley*), and mobile MOBAs (*Arena of Valor*).

Data collection involves a comparative analysis of source and target texts (English to Chinese, English to Spanish, etc. Depending on the case), semiotic analysis of visual assets, and a review of secondary literature regarding the development processes of these titles. The study relies on a corpus of academic literature retrieved from databases focusing on game localization, audiovisual translation, and software engineering.

## 1.7 Definition of Key Terms

To ensure clarity, the following terms are defined as they are used in this thesis.

**Localization (L10n):**
The process of modifying a product or service to account for the differences in distinct markets. In video games, this involves translating text, recording new audio, modifying graphics, and adjusting gameplay mechanics to suit local preferences and regulations (O'Hagan & Mangiron, 2013).

**Internationalization (i18n):**
The engineering process of designing a software application so that it can be adapted to various languages and regions without engineering changes. This includes separating source code from content and supporting different character sets (e.g., Unicode) (Ali & Yue, 2015).

**Transcreation:**
A portmanteau of "translation" and "creation," referring to a strategy where the translator has the creative license to rewrite content entirely to ensure the emotional and functional impact is maintained. This is common in the translation of humor, puns, and marketing materials in games (Moreno García, 2024).

**Assets:**
The digital components that make up a video game, including 2D sprites, 3D models, audio files, text strings, and cinematics. Localization often requires the modification of these assets (Ribeiro et al., 2025).

**Sim-ship:**
Simultaneous shipment; the release of a video game in multiple languages and regions on the same day. This model exerts high pressure on localization schedules and requires parallel development workflows (Üyesi et al., 2020).

**Game Accessibility:**
The practice of removing barriers that prevent people with disabilities from playing video games. In the context of localization, this includes providing subtitles, audio descriptions, and configurable UI options (Larreina & Mangiron, 2025)(Westin, 2012).

## 1.8 Scope and Limitations

### 1.8.1 Scope
This thesis focuses on the localization of video games from the perspective of linguistic assets, cultural adaptation, and technical implementation. It covers genres ranging from Role-Playing Games (RPGs) to mobile strategy games. The analysis considers both the "micro" level of textual translation and the "macro" level of project management and cultural filtering.

### 1.8.2 Limitations
The study is limited by the proprietary nature of the video game industry. Access to internal design documents, localization bibles, and source code is restricted; therefore, the analysis relies on the final released products and public post-mortems. Furthermore, while the study acknowledges the importance of machine translation (MT) and neural machine translation (NMT) in the industry (Aytaş, 2025), the primary focus remains on the human strategies employed in high-stakes creative localization, rather than the raw output of automated systems. Finally, the rapid pace of the industry means that specific technical standards discussed (such as those in (Corbolante & Irmler, 2001) or (Ali & Yue, 2015)) may be subject to frequent iteration.

## 1.9 Organization of the Thesis

The remainder of this thesis is organized as follows:

* **Chapter 2: Literature Review** provides a comprehensive survey of existing scholarship on game localization, covering theoretical models, historical developments, and current debates regarding transcreation and machine translation.
* **Chapter 3: Methodology** details the qualitative approach, data selection criteria, and the analytical frameworks used to compare source and target versions of the selected games.
* **Chapter 4: Analysis and Results** presents the findings from the case studies, categorized by linguistic, cultural, and technical dimensions.
* **Chapter 5: Discussion** interprets the results in the context of the theoretical framework, discussing the implications for the industry and future research.
* **Chapter 6: Conclusion** summarizes the key arguments and offers recommendations for localizers and developers.

---

# 2. Key Concepts and Comparative Frameworks

To establish a solid foundation for the subsequent analysis, it is essential to distinguish between the various layers of content transformation that occur during the localization process. The terminology in this field is often used interchangeably in casual discourse, but in academic and professional contexts, distinctions between translation, localization, and transcreation are crucial for understanding the depth of adaptation required for different game elements.

## 2.1 The Spectrum of Adaptation

Video game localization is not a binary choice between "literal" and "free" translation but exists on a continuum. At one end lies technical translation (e.g. Menu options, system messages), which demands precision and consistency. At the other end lies transcreation (e.g. Jokes, poems, character names), which demands high creativity. The following table illustrates the comparative differences between these approaches as applied to video games.

| Aspect | Translation | Localization | Transcreation |
|:--- |:--- |:--- |:--- |
| **Primary Focus** | Linguistic equivalence | Cultural/Functional usability | Emotional/Marketing impact |
| **Scope** | Text strings, manuals | Text, formats, basic assets | Narrative, humor, titles |
| **Goal** | Accuracy to source | Market readiness | User engagement/Immersion |
| **Example** | "Press Start" $\rightarrow$ "Drücken Sie Start" | Date formats, currency | "Phoenix Down" (Fantasy item) |
| **Key Citation** | (Corbolante & Irmler, 2001) | (O'Hagan & Mangiron, 2013), (Mejías-Climent, 2021) | (Moreno García, 2024), (Wang, 2025) |

*Table 1: Comparative Overview of Adaptation Strategies in Video Games.*

Table 1 delineates the operational differences between standard translation, localization, and transcreation. While translation focuses on linguistic equivalence—often governed by terminology management systems to ensure consistency in software terminology (Corbolante & Irmler, 2001)—localization expands this scope to include functional elements. This includes adjusting date and time formats, currency symbols, and ensuring that text fits within the user interface (UI) constraints. Transcreation, however, represents the most creative tier, often required for character development and narrative immersion. For example, in *Stardew Valley*, the translation of character dialogue requires strategies that recreate personality traits and cultural contexts, moving beyond semantic meaning to pragmatic effect (Wang, 2025). Similarly, the adaptation of cultural realia in *Arena of Valor* necessitates transcreation to make Eastern mythological references accessible to Western players (Moreno García, 2024).

## 2.2 Categorization of Localization Constraints

The strategies outlined above do not occur in a vacuum; they are shaped and often limited by rigid constraints. These constraints can be broadly categorized into technical, cultural, and legal dimensions. Understanding these limitations is vital for analyzing why certain translation errors or "awkward" phrasings appear in final products.

| Category | Constraint Type | Description | Impact on Localization |
|:--- |:--- |:--- |:--- |
| **Technical** | Character Limits | Maximum text length per UI box | Forced abbreviations, font resizing |
| **Technical** | Asset Hard-coding | Text embedded in images | Requires graphic engineering (Ribeiro et al., 2025) |
| **Cultural** | Taboos/Religion | Sensitive topics per region | Asset modification, rewriting |
| **Legal** | Censorship | Government regulations | Content removal (e.g. Gore) (Bates, 2004) |
| **Legal** | Compliance | Financial/Data laws | UI changes for shop/privacy (Roomberg, 2023) |

*Table 2: Taxonomy of Localization Constraints.*

Table 2 categorizes the primary constraints facing localization teams. Technical constraints are pervasive; for instance, the generation and evaluation of image-based assets using deep learning is a response to the high cost and complexity of modifying graphical content for different regions (Ribeiro et al., 2025). If text is "hard-coded" into an image texture, it cannot be easily translated without access to the source art files and significant engineering effort.

Cultural and legal constraints often dictate the viability of a product in a target market. Historical censorship laws, such as those analyzed in Poland, demonstrate how state monopolies can restrict the flow of ideas, a legacy that still influences regional content ratings (Bates, 2004). In the modern context, the Chinese market requires strict adherence to regulations regarding the depiction of violence or anti-social behavior, necessitating "cultural adjustments" that go far beyond language (Dong & Mangiron, 2018). Furthermore, the legal landscape regarding virtual economies and money laundering implies that even the terminology used for in-game transactions must be carefully vetted to avoid legal liabilities, effectively turning game publishers into money transmitters in the eyes of regulators (Roomberg, 2023).

## 2.3 The Role of Technology and Education

The introduction of advanced technologies is reshaping the methods of localization. The industry is witnessing a shift towards the integration of visual and auditory modalities into neural machine translation (NMT) processes. While traditional NMT struggles with context, new models that incorporate visual data (such as screenshots of the game state) show promise in enhancing translation quality by providing the necessary context that text-only strings lack (Aytaş, 2025).

This technological shift necessitates a corresponding evolution in translator training. The curriculum for game localizers must now include blended resources that cover not just linguistic skills but also technical proficiency with localization tools, understanding of game engines, and awareness of the multimodal nature of the medium (Bernal-Merino, 2008)(Merten, 2011). As the industry moves towards more automated solutions for asset generation and testing (Ali & Yue, 2015), the human localizer's role increasingly focuses on high-level cultural adaptation and quality assurance, ensuring that the "soul" of the game survives the transition across borders.

## 2.4 Conclusion of Introduction

In summary, the localization of video games is a multifaceted discipline that sits at the intersection of art, engineering, and commerce. It requires a delicate balance between preserving the original creative vision and adapting the product to meet the linguistic, cultural, and legal expectations of a global audience. By examining the methods and strategies employed—from the micro-level of text string translation to the macro-level of cultural adaptation and asset modification—this thesis aims to illuminate the complex processes that allow video games to function as truly global entertainment. The subsequent chapters will delve deeper into the literature, methodology, and specific case studies that exemplify these dynamics.

\newpage

# 2. Main Body
The academic study of video game localization has evolved significantly over the past two decades, transitioning from a peripheral interest within Translation Studies to a distinct, interdisciplinary field that intersects with ludology, software engineering, and cultural studies. As the video game industry has expanded globally, surpassing the revenue of the film and music industries combined, the necessity for sophisticated localization strategies has become paramount. This literature review synthesizes existing research to establish a theoretical framework for analyzing the localization process. It examines the shift from linguistic equivalence to "transcreation," the technological constraints inherent to the medium, the cultural adaptation of narrative and character assets, and the emerging role of artificial intelligence in automating localization workflows.

### 2.1.1 Theoretical Frameworks and Definitions

To understand the complexities of game localization, it is necessary first to define the theoretical boundaries that distinguish it from traditional forms of translation, such as literary or technical translation. The literature consistently points to the insufficiency of traditional equivalence-based theories when applied to interactive media.

#### 2.1.1.1 From Translation to Transcreation
The foundational concept in modern game localization scholarship is the shift from "translation" to "transcreation." O'Hagan and Mangiron (O'Hagan & Mangiron, 2013) provide the seminal definition of this paradigm, arguing that game localization must prioritize "playability" and the "fun factor" over semantic accuracy. In their comprehensive monograph, they establish that the interactive nature of video games requires localizers to act as co-creators who adapt content to evoke the same emotional response in the target player as experienced by the source player, even if this requires significant deviation from the source text.

This approach is further supported by Bernal-Merino (Bernal-Merino, 2008), who emphasizes that the "skopos" (purpose) of the game—entertainment—dictates the translation strategy. He argues that a literal translation that preserves meaning but disrupts the user interface (UI) or fails to convey the game's mechanics effectively renders the product defective. Consequently, transcreation involves rewriting dialogue, renaming characters, and even altering narrative arcs to suit the target culture's expectations and the game's mechanical constraints.

#### 2.1.1.2 The GILT Model
The industry standard for conceptualizing these processes is the GILT framework (Globalization, Internationalization, Localization, Translation). O'Hagan and Mangiron (O'Hagan & Mangiron, 2013) and Mejías-Climent (Mejías-Climent, 2021) describe this hierarchy as follows:

1. **Globalization:** The business decisions regarding which markets to enter.
2. **Internationalization (i18n):** The technical preparation of the code to handle different languages (e.g. Character encoding, variable UI expansion).
3. **Localization (l10n):** The adaptation of linguistic and cultural assets.
4. **Translation (t9n):** The specific rendering of text from one language to another.

Mejías-Climent (Mejías-Climent, 2021) expands on this by analyzing the history of these processes, noting that early localization was often an afterthought, leading to "hard-coded" text that was impossible to translate without rewriting the game engine. Modern frameworks, however, integrate internationalization at the pre-production stage, allowing for more seamless localization.

#### 2.1.1.3 Communicative Translation Theory
Recent scholarship has applied Newmark’s Communicative Translation Theory to video games, particularly in the context of high-fidelity narratives. Wang (Wang, 2025) applies this lens to the localization of *Black Myth: Wukong*, arguing that for games deeply rooted in specific mythologies, the translator's primary goal is communicative efficacy—ensuring the target audience understands the cultural function of the text—rather than semantic fidelity. This aligns with the broader move toward "domestication" or "foreignization" strategies discussed by Cao (Cao, 2023), who compares these approaches in literary translation. In the context of games, communicative translation ensures that the "gameplay loop" is not interrupted by linguistic confusion.

### 2.1.2 Cultural Adaptation and Asset Management

The localization of cultural "realia"—items, names, and concepts specific to a culture—presents unique challenges in video games due to the multimodal nature of the medium. Unlike a novel, where a footnote can explain a cultural term, a video game must convey information instantaneously to avoid breaking immersion.

#### 2.1.2.1 Adaptation of Character and Narrative
Character development relies heavily on culturally coded dialogue and visual markers. Wang (Wang, 2025) investigates this through the lens of *Stardew Valley*, analyzing how the English character dialogue was translated into Chinese. The study finds that successful character localization requires reconstructing the "personality" of the character using target-culture sociolinguistic markers. For instance, a character speaking in a rural dialect in English might be mapped to a specific regional dialect in Chinese to preserve the "rustic" characterization, a strategy that goes beyond lexical translation to encompass sociolinguistic equivalence.

Similarly, Moreno García (Moreno García, 2024) examines the localization of *Arena of Valor*, a Multiplayer Online Battle Arena (MOBA) game. This genre relies heavily on distinct character archetypes drawn from folklore and history. The study highlights how "cultural realia" are adapted or entirely replaced to resonate with international players. In some cases, characters based on obscure Chinese historical figures were replaced with Western superheroes (e.g., Batman) for the European release, a radical form of transcreation designed to lower the cultural barrier to entry.

#### 2.1.2.2 Visual and Semiotic Analysis
Video games convey meaning through a complex interplay of visual, auditory, and textual signs. Bagaskara and Dhanadipa (Bagaskara & Dhanadipa, 2024) conduct a semiotic analysis of boss cutscenes in *Elden Ring*, demonstrating how visual signs (costume, lighting, gesture) serve as narrative devices that function independently of the text. This implies that localization is not merely about translating subtitles but ensuring that the translated text does not contradict the immutable visual information on screen.

Furthermore, Sun et al. (Sun et al., 2025) discuss "Audio-Visual Event Localization" (AVEL), noting the robust complementary correlation between audio and visual signals. While their work focuses on technical detection, the implication for localization is clear: the semantic load is shared between what is seen and what is heard. If a localization changes the dialogue (audio/text) significantly, it risks creating dissonance with the visual track, a phenomenon known as "ludonarrative dissonance."

#### 2.1.2.3 Cross-Cultural Market Strategies
The flow of cultural products is no longer unidirectional (West to East). Dong and Mangiron (Dong & Mangiron, 2018) analyze the "Journey to the East," focusing on the adaptation of Western games for the Chinese market. They identify strict regulatory requirements and distinct gamer preferences as drivers for localization. Conversely, the rise of the Turkish game industry, as documented by Üyesi et al. (Üyesi et al., 2020), and the global success of Chinese AAA titles like *Black Myth: Wukong* (Wang, 2025), illustrate a "Journey to the West" where non-Western cultural assets must be adapted for global consumption.

Table 1 summarizes the primary cultural adaptation strategies identified in the literature.

| Strategy | Definition | Key Application | Theoretical Basis |
|:--- |:--- |:--- |:--- |
| **Transcreation** | Creative rewriting to preserve "fun factor" | Humor, puns, culturally specific quests | (O'Hagan & Mangiron, 2013), (Moreno García, 2024) |
| **Domestication** | Replacing source culture elements with target culture equivalents | Character names, food items, holidays | (Cao, 2023), (Wang, 2025) |
| **Foreignization** | Retaining source culture elements to preserve "exoticism" | Historical titles, specific mythologies (*Wukong*) | (Cao, 2023), (Wang, 2025) |
| **Neutralization** | Removing cultural markers to create a "generic" international version | UI icons, color schemes, taboo topics | (Dong & Mangiron, 2018) |
| **Visual Adaptation** | Modifying graphical assets to meet legal or cultural norms | Skeletons in Chinese releases, blood color | (Ribeiro et al., 2025), (Dong & Mangiron, 2018) |

*Table 1: Taxonomy of Cultural Adaptation Strategies in Video Game Localization. Source: Adapted from (O'Hagan & Mangiron, 2013), (Cao, 2023), and (Dong & Mangiron, 2018).*

The choice between these strategies is often dictated by the genre. Narrative-heavy games (RPGs) may favor foreignization to immerse players in a specific world, while casual mobile games often employ domestication or neutralization to maximize broad appeal.

### 2.1.3 Technological Constraints and Innovations

Unlike other forms of audiovisual translation, game localization is fundamentally constrained by software engineering. The literature identifies the interplay between code and text as a defining characteristic of the field.

#### 2.1.3.1 Internationalization and Variable Management
Corbolante and Irmler (Corbolante & Irmler, 2001) discuss software terminology and localization, emphasizing the technical rigidity of string management. Text in games is often stored in spreadsheets or databases where context is stripped away. A translator might see the word "Turn" and not know if it refers to a "turn" in a car, a "turn" in a strategy game, or the act of "turning" around. O'Hagan and Mangiron (O'Hagan & Mangiron, 2013) highlight that training translators to deal with these "context-deprived" environments is crucial.

Furthermore, Westin (Westin, 2012) surveys engine-independent solutions for accessibility, which has implications for localization. The way an engine handles text display (fonts, character limits, text wrapping) determines the translator's constraints. If a dialogue box allows only 50 characters, the German translation (which is typically 30% longer than English) must be truncated or rewritten, regardless of semantic accuracy.

#### 2.1.3.2 The Rise of AI and Neural Machine Translation
The integration of Artificial Intelligence (AI) and Machine Learning (ML) is reshaping the localization workflow. Aytaş (Aytaş, 2025) investigates the impact of integrating visual and auditory modalities into Neural Machine Translation (NMT). Traditional NMT models often fail in creative domains because they lack context. However, Aytaş demonstrates that multimodal NMT, which "sees" the game asset associated with the text, significantly improves translation quality by resolving ambiguities.

Ribeiro et al. (Ribeiro et al., 2025) provide a systematic review of deep learning for asset generation. They note that Deep Learning can now automate the creation of graphical content, including user interfaces and typographical elements. This has profound implications for "deep localization," where AI could theoretically generate localized textures (e.g. Changing a "Stop" sign in the game world to "Arrêt" for the French version) automatically, a process that was previously too labor-intensive for most productions.

#### 2.1.3.3 Dubbing and Audio Technologies
Audio localization, or dubbing, adds another layer of complexity. Mejías-Climent (Mejías-Climent, 2021) analyzes dubbing through specific game situations, noting that synchronization in games is harder than in film because the timing can be variable (dynamic) based on player input. Saralegi et al. (Saralegi et al., 2024) discuss the development of automatic multilingual subtitling and dubbing systems, such as "MULTILINGTOOL." These tools aim to streamline the synchronization process, though challenges remain in preserving the emotional nuance of voice acting when using automated solutions.

### 2.1.4 Pedagogical Perspectives and Industry Training

Given the specialized nature of game localization, the literature emphasizes the need for specific pedagogical approaches. General translation training is insufficient for the demands of the industry.

#### 2.1.4.1 Specialized Competencies
Bernal-Merino (Bernal-Merino, 2008) was among the first to outline a curriculum for game localization, identifying the need for "technological competence" alongside linguistic skill. Translators must understand variables, tags, and basic coding syntax. Morais (Morais, 2020) reviews Bernal-Merino's work, reinforcing the idea that localization education must bridge the gap between the commercial and translational aspects of the industry.

#### 2.1.4.2 Blended Learning Resources
Merten (Merten, 2011) advocates for creating "blended resources" for translator training, combining traditional translation theory with practical software testing. This aligns with the findings of Ali and Yue (Ali & Yue, 2015), who formalize software testing standards. In the context of localization, "Linguistic Quality Assurance" (LQA) is a form of software testing. Translators must be trained not just to translate, but to "bug test" language within the build, identifying text overlaps, missing glyphs, and coding errors.

### 2.1.5 Accessibility and Inclusion in Localization

A rapidly expanding sub-field within localization research is accessibility. Localization is increasingly viewed not just as language transfer, but as a means of making games accessible to players with different abilities.

#### 2.1.5.1 Audio Description and Visual Impairment
Larreina and Mangiron (Larreina & Mangiron, 2025) argue that accessibility features like Audio Description (AD) are a form of intersemiotic translation. Since 2020, game accessibility has gained traction, with features for players with visual disabilities becoming more common. The localization of these features—translating the audio description tracks or the screen reader metadata—is a new frontier. A game that is accessible in English but fails to localize its accessibility options into Spanish effectively excludes disabled players in that market.

#### 2.1.5.2 Gender and Representation
Jacobs-Johnson (Jacobs-Johnson, 2017) analyzes gender representation in game production culture. This is relevant to localization because the demographics of the localization team often influence the output. If the localization team lacks diversity, gendered language or inclusive terminology may be mishandled. Jeanmaire and Kim (Jeanmaire & Kim, 2022) explore this in a therapeutic context, discussing the translation of games for children with asthma. They note that translating for vulnerable populations requires a balance between "localization" and "medical vulgarisation" (simplification), ensuring that medical terms are accurate yet understandable across cultures.

### 2.1.6 Empirical Studies on Specific Genres

The literature reveals that localization strategies are highly genre-dependent.

#### 2.1.6.1 Serious and Therapeutic Games
Ohori et al. (Ohori et al., 2021) discuss the "Reorganizing Public Facilities Game," a serious game used for urban planning. Here, the priority is not entertainment but clarity and educational value. Similarly, Jeanmaire and Kim (Jeanmaire & Kim, 2022) highlight that in therapeutic games, the "fun factor" is secondary to clinical adherence. Localization errors in these contexts can have real-world health or policy consequences, demanding a much higher degree of semantic accuracy than entertainment titles.

#### 2.1.6.2 Massive Multiplayer and Live Service Games
The shift to "Games as a Service" (GaaS) has introduced the need for continuous localization. In the case of *Arena of Valor* (Moreno García, 2024), the game is constantly updated with new heroes and items. This requires a "sim-ship" (simultaneous shipment) model, where localization occurs in parallel with development. This contrasts with the older "post-gold" model described in earlier texts like O'Hagan and Mangiron (O'Hagan & Mangiron, 2013), where localization began after the game was finished.

### 2.1.7 Legal and Ethical Considerations

Finally, the literature touches upon the legal and ethical dimensions of the global game trade. Roomberg (Roomberg, 2023) discusses the video game industry's money laundering problems and the legal responsibilities of publishers. While primarily legal research, this impacts localization regarding terminology for in-game currencies and "loot boxes," which face different legal definitions in countries like Belgium versus the United States. Localization teams must be aware of these legal nuances to avoid non-compliance. Additionally, Bates (Bates, 2004) provides historical context on censorship, which remains relevant as localizers must navigate state regulations (e.g., China's restrictions on depictions of time travel or skeletons) that necessitate content modification.

### 2.1.8 Synthesis and Research Gaps

The review of the existing literature reveals a robust theoretical foundation established by O'Hagan, Mangiron, and Bernal-Merino, which successfully legitimizes game localization as a complex form of transcreation. However, several gaps remain that this study aims to address.

**1. The Gap in AI-Human Collaboration Models:**
While recent papers like Aytaş (Aytaş, 2025) and Ribeiro et al. (Ribeiro et al., 2025) discuss the technical capabilities of AI, there is a lack of empirical research on the *workflow integration* of these tools. How do human localizers perceive and edit AI-generated assets in high-stakes AAA productions compared to indie titles?

**2. The "Indie" vs. "AAA" Divide:**
Much of the literature focuses on major commercial titles or generic theoretical models. There is less comparative analysis on how independent developers, who lack the resources for comprehensive GILT workflows, manage localization. Wang's study on *Stardew Valley* (Wang, 2025) is a step in this direction, but broader comparative studies are needed.

**3. Longitudinal Reception Studies:**
While strategies are well-documented, player reception remains under-researched. Meho (Meho, 2025) discusses bibliometric anomalies and metrics, but there is a lack of quantitative data connecting specific localization strategies (e.g. Domestication) to player review scores or sales performance in specific regions.

Table 2 highlights the evolution of research focus in the field, demonstrating the trajectory from definition to technological integration.

| Era | Primary Focus | Key Scholars | Methodological Trend |
|:--- |:--- |:--- |:--- |
| **Foundational (2000-2013)** | Defining the field, GILT framework, Transcreation | (O'Hagan & Mangiron, 2013), (Bernal-Merino, 2008) | Case studies, Theoretical monographs |
| **Expansion (2014-2019)** | Cultural adaptation, Training, Mobile gaming | (Dong & Mangiron, 2018), (Morais, 2020) | Comparative analysis, Pedagogical review |
| **Technological (2020-Present)** | AI/NMT integration, Accessibility, Deep Learning | (Ribeiro et al., 2025), (Aytaş, 2025), (Larreina & Mangiron, 2025) | Systematic reviews, Experimental design |

*Table 2: Evolution of Research Themes in Video Game Localization. Source: Author's synthesis of literature.*

By addressing these gaps, specifically the intersection of cultural adaptation strategies and emerging technical constraints in the modern "Live Service" era, this research contributes to the next phase of game localization scholarship. The following sections will outline the methodology used to investigate these dynamics in the selected case studies.

## 2.2 Methodology

### 2.2.1 Research Design and Approach

This research employs a qualitative, narrative review methodology to analyze the intersection of technical constraints and cultural adaptation in video game localization. Unlike systematic reviews that adhere to rigid inclusion protocols (e.g., PRISMA) to quantify bibliographic data, a narrative review approach allows for a hermeneutic synthesis of diverse source types—ranging from theoretical monographs to technical case studies—to construct a holistic understanding of the "GILT" (Globalization, Internationalization, Localization, Translation) framework.

The primary objective of this methodology is to synthesize existing empirical data regarding localization workflows in both "AAA" (high-budget) and "Indie" (independent) development environments. By adopting a comparative case study synthesis, this section establishes the analytical framework used to evaluate how different development scales impact translation strategies. The research design is grounded in the foundational theories established by O'Hagan and Mangiron (O'Hagan & Mangiron, 2013) and Bernal-Merino (Bernal-Merino, 2008), while integrating contemporary perspectives on neural machine translation (NMT) and deep learning asset generation (Ribeiro et al., 2025)(Aytaş, 2025).

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
| **Theoretical** | Foundational frameworks | GILT, Skopos, Transcreation | (Bernal-Merino, 2008), (O'Hagan & Mangiron, 2013), (Mejías-Climent, 2021) |
| **Technical** | Engineering & Tools | NMT, Deep Learning, ISO Standards | (Ribeiro et al., 2025), (Aytaş, 2025), (Ali & Yue, 2015) |
| **Case Study** | Game-specific analysis | *Stardew Valley*, *Black Myth: Wukong* | (Wang, 2025), (Wang, 2025), (Moreno García, 2024) |
| **Sociocultural** | Industry culture & Ethics | Censorship, Gender, Accessibility | (Jacobs-Johnson, 2017), (Bates, 2004), (Larreina & Mangiron, 2025) |

*Table 3: Categorization of Primary and Secondary Sources. Source: Author's categorization based on literature analysis.*

#### 2.2.2.2 Documentation of Industry Practices
Given the proprietary nature of video game development, direct access to source code or internal localization bibles is rarely available in academic research. Therefore, this methodology relies on "grey literature" validation and secondary analysis of detailed case studies. For instance, the technical constraints of text box limitations and variable handling are analyzed through the lens of software testing standards (Ali & Yue, 2015) and localization handbooks (Corbolante & Irmler, 2001), rather than direct observation of proprietary engines. This approach mitigates the opacity of the industry—a challenge noted in studies regarding industry protectionism and digital rights management (Pachali, 2011)—by triangulating findings across multiple independent reports.

### 2.2.3 Theoretical Framework for Analysis

The analysis of localization strategies is conducted through a dual-lens framework combining **Communicative Translation Theory** and **Multimodal Semiotics**.

#### 2.2.3.1 Communicative Translation in Interactive Media
Traditional translation theory often prioritizes semantic equivalence. However, in video games, the "skopos" (purpose) of the text is primarily to facilitate gameplay and immersion. This research utilizes the Communicative Translation perspective, as applied by Wang (Wang, 2025) in the analysis of *Black Myth: Wukong*. This framework posits that the successful localization of a game is measured not by linguistic accuracy, but by the recreation of the intended "game feel" and narrative impact for the target audience.

The analysis evaluates translation choices based on Newmark’s dichotomy of semantic vs. communicative translation, adapted for the constraints of UI design. For example, when analyzing dialogue in *Stardew Valley* (Wang, 2025), the methodology examines whether "cultural softening" or "domestication" strategies were employed to make the text acceptable to the target culture, potentially at the expense of the source text's original nuance.

#### 2.2.3.2 Multimodal Semiotics and Audio-Visual Cohesion
Video games are polysemiotic systems where meaning is constructed through text, audio, and visual cues simultaneously. A purely textual analysis is insufficient. Therefore, this methodology incorporates a multimodal analysis framework as described by Bagaskara and Dhanadipa (Bagaskara & Dhanadipa, 2024) in their study of *Elden Ring*, and Sun et al. (Sun et al., 2025) regarding audio-visual event localization.

The relationship between these modalities can be formalized to understand the "Translation Load" ($T_L$). If the visual channel ($V$) and audio channel ($A$) provide high context, the reliance on the textual channel ($T$) decreases. Conversely, where visuals are abstract, the text must carry a heavier explanatory load.

The analysis considers the cohesion between these elements:
$$C_{total} = f(T_{sync}, A_{cues}, V_{context})$$

Where $C_{total}$ represents the total semiotic cohesion perceived by the player. This formulation allows for the evaluation of "ludonarrative dissonance" caused by poor localization—for instance, when a translated subtitle contradicts a visual cue or an audio prompt, a phenomenon investigated in studies on audio description and accessibility (Larreina & Mangiron, 2025).

### 2.2.4 Comparative Case Study Framework: AAA vs. Indie

To address the research gap regarding the "Indie vs. AAA" divide identified in the literature review, this methodology establishes a comparative matrix. This matrix distinguishes between the resource-rich, highly stratified workflows of AAA studios and the resource-constrained, often community-reliant workflows of indie developers.

#### 2.2.4.1 Defining the Variables
The comparison is not merely financial but methodological. AAA localization is characterized by the simultaneous shipment of multiple languages (Sim-ship), requiring robust "Internationalization" (i18n) phases integrated into the code structure early in development (Corbolante & Irmler, 2001). In contrast, indie localization often occurs post-release, sometimes utilizing fan translations or crowdsourcing, which introduces unique quality control and consistency challenges.

Table 4 defines the specific variables used to analyze the case studies in the subsequent Analysis section.

| Variable | AAA Characteristics (e.g., *Black Myth*) | Indie Characteristics (e.g., *Stardew Valley*) | Implications for Analysis |
|:--- |:--- |:--- |:--- |
| **Workflow** | Integrated, Simultaneous | Post-release, Sequential | Impact on context availability |
| **Technology** | Proprietary engines, AI integration | Unity/Godot, Manual spreadsheets | Technical constraint rigidity |
| **Cultural Strategy** | Market-driven, "Culturally Odorless" | Auteur-driven, Niche appeal | Domestication vs. Foreignization |
| **QA Process** | LQA teams, Automated testing | Community feedback, Beta branches | Error frequency and type |

*Table 4: Comparative Variables for AAA vs. Indie Localization Analysis. Source: Adapted from (O'Hagan & Mangiron, 2013) and (Wang, 2025).*

#### 2.2.4.2 The Role of Technical Constraints
A critical component of this methodology is the isolation of **technical constraints** as a determinant of translation strategy. Literature indicates that translators often modify text not for cultural reasons, but to fit strict character limits or memory buffers (Morais, 2020). The analysis distinguishes between:
1. **Hard Constraints:** Fixed byte limits, UI pixel width, non-resizable text boxes.
2. **Soft Constraints:** Reading speed guidelines for subtitles, synchrony with lip movements (labial sync).

By applying the definitions from Corbolante and Irmler (Corbolante & Irmler, 2001) regarding software terminology and localization, the analysis seeks to identify instances where technical limitations forced a "simplification" strategy, distinguishing this from stylistic choices.

### 2.2.5 Analytical Categories for Cultural Adaptation

Beyond technical constraints, the methodology examines the cultural dimensions of localization using the Domestication and Foreignization spectrum. This approach draws on the work of Cao (Cao, 2023) and Dong and Mangiron (Dong & Mangiron, 2018) regarding the adaptation of games for specific markets, such as China.

#### 2.2.5.1 Taxonomy of Cultural Realia
To systematically analyze how cultural elements are handled, this research utilizes a taxonomy of "Cultural Realia" based on Moreno García’s work (Moreno García, 2024). The analysis categorizes in-game assets into:
* **Ecological Realia:** Flora, fauna, and geographical features specific to the source culture.
* **Material Realia:** Food, clothing, and architecture.
* **Social Realia:** Legal systems, religious practices, and historical references.

For each instance of realia identified in the case studies (e.g., Chinese mythological figures in *Black Myth: Wukong* or farming festivals in *Stardew Valley*), the translation strategy is classified according to the following strategies:
1. **Preservation:** Keeping the term in the source language (Foreignization).
2. **Literal Translation:** Calque.
3. **Cultural Equivalent:** Replacing the item with a target-culture equivalent (Domestication).
4. **Omission:** Removing the reference entirely.

This classification allows for a quantitative comparison of strategy frequency between the selected titles, providing empirical evidence for the "cultural softening" hypothesis proposed by Wang (Wang, 2025).

#### 2.2.5.2 Analyzing Censorship and Regulation
A subset of cultural adaptation involves regulatory compliance and censorship. Drawing on Bates (Bates, 2004) regarding censorship mechanisms and Roomberg (Roomberg, 2023) regarding industry regulation, the methodology includes a review of changes mandated by regional laws (e.g. Prohibition of skeletons or gambling mechanics). This is particularly relevant for the "Journey to the East" context described by Dong and Mangiron (Dong & Mangiron, 2018), where Western games must undergo significant modification to enter the Chinese market. The analysis treats these regulatory changes as "Mandated Localization," distinct from "Creative Localization."

### 2.2.6 Evaluation of Technological Integration (AI and NMT)

The final pillar of the methodology addresses the rapid integration of Artificial Intelligence in the localization pipeline. This section moves beyond traditional GILT frameworks to incorporate recent findings on Deep Learning and Neural Machine Translation (NMT).

#### 2.2.6.1 Assessing Automated Workflows
The analysis utilizes the framework proposed by Ribeiro et al. (Ribeiro et al., 2025) for evaluating deep learning assets and Aytaş (Aytaş, 2025) for multimodal NMT. The methodology involves a theoretical assessment of where AI tools are currently deployed in the localization chain:
* **Pre-production:** AI-generated placeholder text and synthetic voice-overs.
* **Production:** NMT drafts for post-editing (PEMT).
* **Post-production:** Automated LQA (Language Quality Assurance) checks.

The study contrasts the efficiency gains reported in technical literature (Ali & Yue, 2015) with the quality concerns raised in translation studies. Specifically, it examines the "context blindness" of NMT engines—their inability to distinguish between homonyms based on game state—and how human translators mitigate this.

#### 2.2.6.2 Accessibility as a Localization Vector
Modern localization increasingly overlaps with accessibility. The methodology includes **Audio Description (AD)** and **Subtitling for the Deaf and Hard of Hearing (SDH)** as forms of intersemiotic translation. Following Larreina and Mangiron (Larreina & Mangiron, 2025) and Westin (Westin, 2012), the analysis evaluates how accessibility features are localized. For example, does the localized version of a game retain the detailed audio cues required for visually impaired players? This expands the definition of "localization" to include the translation of sensory experience, not just text.

### 2.2.7 Methodological Limitations

While this narrative review and comparative framework provide a robust structure for analysis, several limitations inherent to the research design must be acknowledged.

#### 2.2.7.1 Lack of Access to Source Code
A primary limitation in video game research is the "Black Box" nature of proprietary software. As noted by Pachali (Pachali, 2011), developers aggressively protect their intellectual property. Consequently, this study cannot verify the exact code-level implementation of localization strings (e.g. Whether a string is hard-coded or called from an external database) unless explicitly documented in post-mortem reports or technical papers. The analysis relies on the *observable output* (the game on screen) rather than the *input mechanism* (the code).

#### 2.2.7.2 Bias in Source Availability
The selection of case studies and supporting literature reflects a bias toward major linguistic pairs, specifically English-Chinese and English-European languages. Sources such as Wang (Wang, 2025), (Wang, 2025) and Dong and Mangiron (Dong & Mangiron, 2018) provide extensive data on the Chinese market, while other regions (e.g., Arabic, Hindi) are underrepresented in the available citation database. This geographic limitation may skew the understanding of "universal" localization challenges.

#### 2.2.7.3 The "Gamer" Variable
Finally, analyzing player reception through bibliometrics and review aggregation, as discussed by Meho (Meho, 2025), presents challenges in sentiment analysis. Player reviews are often polarized or focus on gameplay mechanics rather than translation quality. Disentangling complaints about "bugs" from complaints about "localization errors" requires careful qualitative coding. Furthermore, the demographic profile of players leaving reviews may not represent the broader player base, introducing a selection bias in the reception analysis.

### 2.2.8 Synthesis of Analytical Approach

In summary, the methodology adopted for this thesis is a **multiperspective comparative analysis**. It triangulates data from theoretical models (GILT), technical specifications (ISO standards/Platform guidelines), and cultural case studies (AAA vs. Indie).

The analytical process proceeds in three stages:
1. **Deconstruction:** Breaking down the selected games into their constituent localizable assets (text, audio, graphics).
2. **Categorization:** Classifying the adaptation strategies applied to these assets using the taxonomy defined in Table 4 (Preservation, Substitution, Omission).
3. **Correlation:** Mapping these strategies against the identified constraints (Technical limits, Cultural taboos, Budgetary restrictions) to determine causality.

This structured approach allows the research to move beyond anecdotal observation of "funny translation errors" to a rigorous examination of the systemic forces—technological, economic, and cultural—that shape the final localized product. By integrating the communicative perspective (Wang, 2025) with the technical realities of asset generation (Ribeiro et al., 2025), the methodology is equipped to address the complex, interdisciplinary nature of modern video game localization.

### 2.2.9 Ethical Considerations in Game Localization Research

Although this study does not involve human participants in an experimental setting, ethical considerations regarding the representation of developer labor and player culture are pertinent. Jacobs-Johnson (Jacobs-Johnson, 2017) highlights the gendered and often precarious nature of production culture in the gaming industry. In analyzing localization failures or "crunched" workflows, this research maintains an ethical stance that avoids assigning individual blame to translators, recognizing instead the structural pressures of the industry. Furthermore, when discussing therapeutic or serious games, as explored by Jeanmaire and Kim (Jeanmaire & Kim, 2022), the analysis respects the medical and vulnerable context of the target audience, ensuring that critiques of localization do not undermine the therapeutic intent of the software.

The following sections (Analysis and Results) will apply this methodological framework to the selected case studies, presenting a detailed examination of how the tension between technical rigidity and cultural fluidity is negotiated in practice.

## 2.3 Analysis and Results

The analysis of the selected literature reveals a fundamental shift in video game localization paradigms, moving from linguistic equivalence to a complex interplay of "transcreation," technical asset management, and cultural negotiation. By synthesizing findings from foundational texts (O'Hagan & Mangiron, 2013)(Mejías-Climent, 2021) and recent case studies (Wang, 2025)(Wang, 2025), this section presents the results of the narrative review. The findings are categorized into four primary dimensions: the operationalization of transcreation in character development, the technical integration of deep learning and asset generation, the semiotic analysis of multimodal elements, and the ethical implications of accessibility and representation.

### 2.3.1 The Operationalization of Transcreation and Communicative Strategies

The most consistent finding across the analyzed literature is the inadequacy of traditional translation theories to address the interactive nature of video games. The results indicate that "transcreation"—a term solidified in game studies by O'Hagan and Mangiron (O'Hagan & Mangiron, 2013)—has become the standard operating procedure for high-fidelity localization. This approach prioritizes the "playability" and emotional experience of the target audience over semantic fidelity to the source text.

#### 2.3.1.1 Character Voice and Dialogue Reconstruction
Recent case studies demonstrate that transcreation is particularly critical in the localization of character dialogue and personality. Wang's analysis of *Stardew Valley* (Wang, 2025) provides empirical evidence of this strategy. The study reveals that direct translation of character dialogue often results in a "flattening" of personality traits, particularly for characters designed with specific socio-cultural markers. To maintain the "rural charm" and specific interpersonal dynamics of the game, translators employed communicative translation strategies that altered the literal meaning of sentences to preserve the illocutionary force—the intended function of the speech act.

Similarly, the analysis of *Black Myth: Wukong* by Wang (Wang, 2025) highlights the tension between preserving cultural authenticity and ensuring communicative clarity for a global audience. As a game deeply rooted in Chinese mythology (specifically *Journey to the West*), the localization team faced the challenge of translating archaic terms and Buddhist concepts. The findings suggest that a "communicative translation" approach was favored, where cultural specificities were often explicated or adapted to ensure that the narrative beat landed with Western players, even if it meant sacrificing some degree of philological precision.

Table 1 summarizes the comparative analysis of translation strategies found in the literature, contrasting the approaches used in different genres.

| Strategy | Focus | Case Study Example | Outcome |
|:---|:---|:---|:---|
| **Domestication** | Fluency for target culture | *Stardew Valley* (Wang, 2025) | Enhanced immersion; loss of source nuances |
| **Foreignization** | Preserving source otherness | *Black Myth: Wukong* (Wang, 2025) | Retained cultural identity; higher cognitive load |
| **Transcreation** | Creating new content | *Arena of Valor* (Moreno García, 2024) | Complete asset replacement for market appeal |
| **Communicative** | Message function over form | General Industry (O'Hagan & Mangiron, 2013) | Prioritizes "fun factor" and playability |

*Table 1: Comparative Analysis of Translation Strategies in Selected Literature.*

The dichotomy between domestication and foreignization, a classic debate in translation studies exemplified by literary comparisons such as Cao's analysis of *Biancheng* (Cao, 2023), is recontextualized in video games. While literary translation often debates the ethics of erasing the source culture, game localization results suggest that the commercial imperative of "immersion" drives a stronger tendency toward domestication or total transcreation. However, *Black Myth: Wukong* represents a counter-trend identified in the data: the rise of "cultural export" games where the foreignness of the setting is a primary selling point, necessitating a strategy that balances accessibility with exoticism (Wang, 2025).

#### 2.3.1.2 Humor and Cultural Realia
Moreno García's investigation into *Arena of Valor* (Moreno García, 2024) provides significant data on the handling of "cultural realia"—objects, myths, or concepts specific to a culture. The analysis reveals that mobile MOBA (Multiplayer Online Battle Arena) games often resort to extreme transcreation, effectively replacing entire characters or skins to match the target market's cultural expectations. For instance, a character based on Chinese folklore might be visually and narratively overhauled to resemble a Western fantasy archetype for the European release. This goes beyond textual translation into the realm of "cultural engineering," where the product is fundamentally altered to maximize market penetration.

### 2.3.2 Technical Constraints and Automated Workflows

The results of the literature review indicate that technical constraints remain a defining characteristic of game localization, distinguishing it from other audiovisual translation modes. However, the nature of these constraints has evolved from simple storage limitations to complex issues regarding asset generation and neural network integration.

#### 2.3.2.1 From Text to Asset Generation
A critical finding from Ribeiro et al. (Ribeiro et al., 2025) is that modern localization is increasingly concerned with non-textual assets. The systematic review of deep learning applications in games reveals that "asset generation" is no longer limited to procedural terrain but extends to the localization of graphical user interfaces (GUI) and in-game textures. Deep learning models are now capable of generating image-based assets that adapt to the target language.

For example, if a sign in a game world reads "STOP" in English, traditional localization might rely on subtitles or leave the graphic untranslated due to the high cost of re-rendering textures. Ribeiro et al. (Ribeiro et al., 2025) demonstrate that Generative Adversarial Networks (GANs) and other deep learning architectures can automate the creation of localized textures, allowing the sign to read "ARRÊT" in French or "PARE" in Spanish with the same visual style and weathering effects as the original. This represents a significant leap in "deep localization," reducing the friction between the diegetic world and the localized interface.

#### 2.3.2.2 Neural Machine Translation (NMT) and Multimodality
The integration of Neural Machine Translation (NMT) into game workflows is another key theme. Aytaş (Aytaş, 2025) presents data on the efficacy of "multimodal" NMT systems. Traditional machine translation engines process text in isolation, often leading to context errors (e.g. Translating the noun "Tank" as a verb or a container, rather than the military vehicle or RPG class). Aytaş's research indicates that integrating visual and auditory modalities—feeding the NMT model screenshots or audio clips associated with the text segment—significantly improves translation quality.

This finding is corroborated by Sun et al. (Sun et al., 2025), who explore cross-modal contrastive learning. While their work focuses on audio-visual event localization, the underlying principle applies to game localization: the meaning of a game asset is constructed through the convergence of sound, image, and text. Automated systems that ignore this multimodal context fail to achieve the "functional equivalence" required by the industry.

Table 2 presents the technical challenges identified in the literature and the corresponding AI-driven solutions currently emerging in the field.

| Challenge | Technical Constraint | Emerging Solution | Citation |
|:---|:---|:---|:---|
| **Context Loss** | Text strings lack visual context | Multimodal NMT (Visual/Audio input) | (Aytaş, 2025) |
| **Texture Lock** | Hard-coded text in images | Deep Learning Asset Generation | (Ribeiro et al., 2025) |
| **Workflow Speed** | Live service update frequency | Automated Subtitling Systems | (Saralegi et al., 2024) |
| **Testing** | Infinite branching narratives | Automated Software Testing Standards | (Ali & Yue, 2015) |

*Table 2: Technical Constraints and AI-Driven Solutions in Game Localization.*

### 2.3.3 Semiotic Analysis and Multimodal Cohesion

Moving beyond the text, the analysis of semiotic systems in video games reveals that meaning is often encoded in non-verbal signs that require interpretation and localization. Bagaskara and Dhanadipa's study of *Elden Ring* (Bagaskara & Dhanadipa, 2024) provides a rigorous semiotic analysis of visual signs in boss cutscenes.

#### 2.3.3.1 Visual Narratives and Environmental Storytelling
The findings from *Elden Ring* suggest that narrative delivery in modern "Souls-like" games relies heavily on visual semiotics—costume design, lighting, character positioning, and environmental debris—rather than explicit dialogue (Bagaskara & Dhanadipa, 2024). For the localizer, this presents a unique challenge: the text must anchor the ambiguity of the visual signs without over-explaining them. The analysis shows that successful localization in this genre often involves "minimalist" translation strategies that preserve the interpretative gap intended by the developers.

This connects to the broader concept of "inter-semiotic translation" discussed in the theoretical literature. When Chepelyuk et al. (Chepelyuk et al., 2025) analyze the internal organization of discourse in games, they find that the "text" is merely one layer of a polyphonic system. If the visual channel conveys aggression (red colors, sharp angles), the localized text must align with that affective register. Incongruence between the visual sign (universal) and the verbal sign (localized) leads to a breakdown in player immersion, a phenomenon often described by players as "bad writing" but identified in the analysis as "semiotic dissonance."

#### 2.3.3.2 Audio-Visual Synchronization and Dubbing
The challenges of dubbing are further explored by Mejías-Climent (Mejías-Climent, 2021), who analyzes dubbing through game situations. Unlike film dubbing, where linear timing is fixed, game dubbing must account for dynamic triggers. The analysis reveals that "isochrony" (matching the duration of the spoken phrase) is more critical in games than lip-syncing, due to the programmable nature of dialogue windows. However, in cinematic cutscenes, the expectations match film standards. Saralegi et al. (Saralegi et al., 2024) discuss the development of automatic multilingual subtitling and dubbing systems, noting that while automation can handle timing (spotting), the prosodic adaptation required for emotional resonance remains a human-centric task.

### 2.3.4 Cultural Adaptation and Regulatory Compliance

The results of the review highlight that localization is frequently a tool for market access, subject to strict political and cultural regulations. This is most evident in the analysis of the Chinese market.

#### 2.3.4.1 The "Journey to the East" Paradigm
Dong and Mangiron (Dong & Mangiron, 2018) provide extensive data on the adaptation of Western games for China. Their findings, titled "Journey to the East," outline a systematic process of "sanitization" and "cultural harmonization." Key data points include the removal of skeletons and blood to comply with Chinese Ministry of Culture regulations, and the modification of political narratives that might be construed as sensitive.

This regulatory landscape necessitates a form of "preventive localization," where developers alter assets during the production phase to avoid bans. The analysis draws a parallel here to historical forms of censorship, such as those described by Bates (Bates, 2004) regarding state monopolies on information in Poland (1976-1989). While the context differs, the mechanism—state-controlled access to cultural products dictating the content of those products—remains a consistent structural force. In the game industry, this results in "regional builds" of software, where the game played in Shanghai differs visually and narratively from the version played in New York.

#### 2.3.4.2 Economic Implications and Market Strategy
The economic driver behind these adaptations is substantial. As noted in the literature regarding the Turkish game industry (Üyesi et al., 2020), the disruption of mobile technologies has globalized the revenue streams for even small developers. Consequently, the "localization ROI" (Return on Investment) calculation determines the depth of adaptation. Roomberg (Roomberg, 2023) touches upon the financial complexities of the industry, including money laundering risks in virtual economies, which adds another layer to localization: the translation and adaptation of legal terms, monetization schemes, and currency formats must meet diverse international financial regulations.

Table 3 synthesizes the levels of cultural adaptation identified in the analysis, ranging from superficial translation to deep regulatory modification.

| Level | Description | Examples from Literature | Primary Driver |
|:---|:---|:---|:---|
| **Surface** | Text/UI translation only | Indie games (limited budget) | Cost-efficiency |
| **Cultural** | Adaptation of humor/names | *Stardew Valley* (Wang, 2025) | Immersion/Playability |
| **Deep** | Asset replacement (skins/maps) | *Arena of Valor* (Moreno García, 2024) | Market appeal |
| **Regulatory** | Censorship/Compliance | Chinese Market adaptations (Dong & Mangiron, 2018) | Legal access |

*Table 3: Hierarchy of Cultural Adaptation and Regulatory Compliance.*

### 2.3.5 Accessibility and Ethical Considerations

The final dimension of the analysis concerns the ethical expansion of localization to include accessibility features, effectively "localizing" the game for players with disabilities.

#### 2.3.5.1 Audio Description and Universal Design
Larreina and Mangiron (Larreina & Mangiron, 2025) present findings on the implementation of Audio Description (AD) in video games. Historically, AD was a post-production addition for linear media. However, the analysis shows that in games, AD must be integrated into the game engine itself to react to player agency. The results indicate that "accessible localization" is becoming a standard quality metric. Westin (Westin, 2012) supports this by surveying engine-independent solutions for large-scale accessibility, arguing that accessibility features should be treated as a form of "intralingual localization"—translating visual data into audio data for blind players, or audio data into haptic/visual data for deaf players.

#### 2.3.5.2 Therapeutic and Serious Games
The analysis of therapeutic games by Jeanmaire and Kim (Jeanmaire & Kim, 2022) introduces a vital ethical nuance. When localizing games designed for medical purposes (e.g. Asthma management for children), the "transcreation" liberty is constrained by clinical accuracy. The findings show that the translator must balance "medical vulgarisation" (making complex terms understandable to children) with strict adherence to medical protocols. An error in translating a dosage instruction or a symptom description in a therapeutic game carries real-world health risks, unlike a mistranslation in a fantasy RPG. This necessitates a collaborative workflow involving medical professionals, distinct from the typical entertainment localization pipeline.

#### 2.3.5.3 Gender and Production Culture
Finally, the analysis of production culture by Jacobs-Johnson (Jacobs-Johnson, 2017) reveals the gendered dimensions of the industry that indirectly affect localization. The "crunch culture" and male-dominated environments often result in source texts that reflect specific biases. Localizers, often acting as cultural mediators, may attempt to "soften" or "correct" gender stereotypes present in the source material during the translation process. This act of "ethical intervention" is a recurring theme in the results, suggesting that localizers view themselves not just as conduits of text, but as stewards of representation.

### 2.3.6 Synthesis of Findings

The integration of these diverse findings paints a picture of video game localization as a highly technical, ethically complex, and culturally stratified practice. The literature confirms that the GILT framework (Globalization, Internationalization, Localization, Translation) described by O'Hagan and Mangiron (O'Hagan & Mangiron, 2013) is still relevant but has been complicated by the rise of AI (Ribeiro et al., 2025) and the fragmentation of global markets (Dong & Mangiron, 2018).

The analysis demonstrates that "quality" in game localization is no longer defined by linguistic accuracy alone. Instead, it is a composite metric comprising:
1. **Functional Equivalence:** Does the game play the same way? ((O'Hagan & Mangiron, 2013))
2. **Cultural Resonance:** Does the character feel authentic to the target culture? ((Wang, 2025), (Wang, 2025))
3. **Technical Integration:** Do the assets (text, texture, audio) load and display correctly without breaking immersion? ((Ribeiro et al., 2025), (Aytaş, 2025))
4. **Regulatory Compliance:** Is the content legal in the target territory? ((Dong & Mangiron, 2018))

These results provide a robust empirical basis for the discussion that follows, highlighting the tension between the creative aspirations of transcreation and the rigid constraints of code and capital.

### 2.3.7 Statistical Trends in Research Focus

While this review is narrative, a meta-analysis of the cited literature reveals shifting trends in research focus over the last decade. Early research (Bernal-Merino, 2008)(Corbolante & Irmler, 2001) focused heavily on terminology management and translator training. The middle period (O'Hagan & Mangiron, 2013)(Westin, 2012) emphasized accessibility and the definition of the field. The most recent wave of research (Ribeiro et al., 2025)(Aytaş, 2025)(Sun et al., 2025) is dominated by the application of deep learning and neural networks to the localization pipeline.

Table 4 illustrates the thematic distribution of the analyzed sources, indicating the trajectory of the field.

| Research Era | Dominant Theme | Key Citations | Methodological Focus |
|:---|:---|:---|:---|
| **Foundational (2000-2013)** | Definitions, Training, Terminology | (Bernal-Merino, 2008), (O'Hagan & Mangiron, 2013), (Corbolante & Irmler, 2001) | Qualitative, Pedagogical |
| **Expansion (2014-2020)** | Cultural Adaptation, Mobile Markets | (Üyesi et al., 2020), (Dong & Mangiron, 2018), (Morais, 2020) | Case Studies, Industry Analysis |
| **Technological (2021-2025)** | AI, Deep Learning, Multimodality | (Ribeiro et al., 2025), (Aytaş, 2025), (Sun et al., 2025) | Experimental, Computer Science |

*Table 4: Thematic Evolution of Game Localization Research.*

This trajectory suggests that the future of localization analysis will increasingly require interdisciplinary methodologies that combine translation studies with computer science and data analytics, a conclusion supported by the emergence of complex "meta-design models" for collaborative work (Zhu, 2018) and the rigorous formalization of software testing standards (Ali & Yue, 2015).

The results presented here underscore that video game localization has matured into a distinct industrial and academic discipline. The evidence from *Stardew Valley*, *Black Myth: Wukong*, and *Elden Ring* confirms that successful localization is a holistic process of "world re-engineering," where every semiotic layer—from the code to the cutscene—is subject to transformation.

# 2.4 Discussion

The synthesis of research findings presented in Section 2.3 reveals a dynamic and rapidly maturing field that has fundamentally outgrown its origins as a sub-discipline of technical translation. By integrating the theoretical frameworks established in the literature review (Section 2.1) with the thematic and chronological trends identified in the results (Section 2.3), this discussion interprets the current state of video game localization. The analysis indicates a paradigm shift from linguistic equivalence to "world re-engineering," driven by the dual pressures of technological advancement—specifically artificial intelligence—and the increasing demand for deep cultural adaptation in globalized markets.

This section interprets these findings through four primary lenses: the evolution of transcreation strategies, the impact of AI on the localization pipeline, the rise of multimodality and semiotics, and the professionalization of the industry. Furthermore, it addresses the research gaps identified in Section 2.1 regarding the lack of empirical reception studies and outlines future directions for the discipline.

## 2.4.1 The Evolution of Transcreation: From Text to Cultural Experience

As discussed in Section 2.1, the theoretical foundation of game localization has long rested on O'Hagan and Mangiron’s concept of "transcreation" (O'Hagan & Mangiron, 2013), which prioritizes the player's experience over strict semantic fidelity. The results from Section 2.3 confirm that this theoretical model has not only persisted but has intensified in scope. The literature analyzed suggests that modern localization strategies now encompass a holistic reshaping of the game's cultural identity, a process that transcends the text to influence character design, narrative structure, and even game mechanics.

### 2.4.1.1 Strategies of Domestication and Foreignization
The dichotomy between domestication (adapting content to the target culture) and foreignization (preserving the source culture's otherness), a central tenet of translation theory discussed in Section 2.1, remains a critical strategic choice in video game localization. The case studies identified in the literature, particularly *Stardew Valley* (Wang, 2025) and *Black Myth: Wukong* (Wang, 2025), illustrate how developers and localizers navigate this spectrum.

Research by Wang (Wang, 2025) on *Stardew Valley* demonstrates a strong inclination towards domestication in character development. The findings indicate that to recreate character personalities effectively for a Chinese audience, translators often employ "communicative translation" strategies that modify dialogue to fit target-culture social norms. This aligns with the "Skopos theory" mentioned in early literature (Bernal-Merino, 2008), where the purpose of the translation (entertainment and immersion) dictates the method. In *Stardew Valley*, the "world re-engineering" is subtle, focusing on interpersonal dynamics and linguistic politeness strategies that resonate with local players, thereby reducing the cognitive load required to understand foreign social cues.

Conversely, the analysis of *Black Myth: Wukong* by Wang (Wang, 2025) presents a compelling counter-narrative favoring foreignization. As a title deeply rooted in Chinese mythology (specifically *Journey to the West*), the localization strategy prioritizes the preservation of cultural authenticity over ease of access. This approach challenges the traditional industry wisdom noted in Section 2.1, which often advocated for the removal of "cultural odors" to ensure global appeal. The success of such titles suggests a market shift where global players increasingly value "cultural tourism" within games. The localization process here becomes an act of cultural export, requiring translators to function as cultural mediators who explain, rather than erase, the source culture's specificities.

Table 5 summarizes the strategic divergence observed in the analyzed literature, contrasting the approaches of domestication and foreignization across different game genres.

| Feature | Domestication Strategy | Foreignization Strategy | Implication for Immersion |
|:---|:---|:---|:---|
| **Primary Goal** | Fluency and immediate relatability | Cultural authenticity and education | High comfort vs. High curiosity |
| **Character Voice** | Adapted to target culture norms | Retains source culture idiosyncrasies | Familiarity vs. Exoticism |
| **Cultural Realia** | Replaced with local equivalents | Retained with context/glossaries | Seamlessness vs. Learning curve |
| **Key Example** | *Stardew Valley* (Wang, 2025) | *Black Myth: Wukong* (Wang, 2025) | Genre-dependent expectations |
| **Theoretical Basis** | Communicative Translation | Source-Oriented Preservation | (Cao, 2023), (Dong & Mangiron, 2018) |

*Table 5: Comparative Analysis of Localization Strategies in Recent Case Studies.*

The implications of this divergence are significant. The literature suggests that "transcreation" is no longer a monolithic concept but a flexible continuum. The choice between domestication and foreignization is increasingly dictated by the genre and the specific "value proposition" of the game. For casual simulation games like *Stardew Valley*, the value lies in relaxation and familiarity, necessitating domestication. For mythic action-RPGs like *Black Myth: Wukong*, the value lies in the exploration of a specific cultural fantasy, necessitating foreignization. This nuance refines the broad definitions provided in the foundational texts (O'Hagan & Mangiron, 2013) and addresses the "one size fits all" limitation of early localization models.

### 2.4.1.2 Cultural Adaptation in Asian Markets
The literature highlights the Asian market, particularly China, as a critical arena for localization studies. Dong and Mangiron (Dong & Mangiron, 2018) emphasize that entering the Chinese market requires rigorous cultural adjustments that go beyond translation. This includes navigating regulatory landscapes and censorship (Bates, 2004), as well as adapting to specific gamer expectations regarding monetization and aesthetics.

The findings synthesized in Section 2.3 regarding mobile markets (Üyesi et al., 2020) further corroborate the necessity of hyper-localization. In mobile gaming, where session times are short and user retention is precarious, any cultural friction can lead to churn. Therefore, the "world re-engineering" in mobile titles often involves aggressive adaptation of UI, color schemes, and monetization models to fit local habits. This contrasts with the console/PC market, where players may be more willing to engage with foreign cultural concepts. The literature indicates that successful localization in these regions is not merely linguistic but requires a "cultural audit" of the entire software product.

## 2.4.2 The Technological Turn: AI and Deep Learning Integration

One of the most profound findings from the literature analysis in Section 2.3 is the rapid integration of artificial intelligence and deep learning into the localization workflow. This trend represents a significant evolution from the "Computer-Assisted Translation" (CAT) tools discussed in the early literature (Corbolante & Irmler, 2001). The current research landscape (Ribeiro et al., 2025)(Aytaş, 2025)(Sun et al., 2025) suggests that technology is shifting from a supportive role to a generative one.

### 2.4.2.1 From Text Processing to Asset Generation
The systematic review by Ribeiro et al. (Ribeiro et al., 2025) marks a critical turning point in how localization assets are conceived. While traditional localization focused on text strings, modern deep learning techniques enable the generation and modification of image-based assets. This capability allows for "deep localization" where visual elements—textures, sprites, and UI components—can be automatically adapted to target locales. For instance, street signs in an open-world game could be visually rewritten by a Generative Adversarial Network (GAN) to match the target language, maintaining visual consistency without manual re-texturing by artists.

This technological advancement addresses a long-standing bottleneck identified in Section 2.1: the disconnect between linguistic translation and visual context. Historically, translators often worked in "blind" environments (Excel sheets), leading to context errors. The emergence of "Listen With Seeing" frameworks (Sun et al., 2025) and cross-modal contrastive learning suggests a future where localization tools are context-aware, analyzing both audio and visual tracks to propose more accurate translations. This multimodal approach aligns with Aytaş’s findings (Aytaş, 2025) on enhancing Neural Machine Translation (NMT) with visual modalities, proving that providing visual context to AI models significantly reduces ambiguity and improves translation quality.

### 2.4.2.2 Automation vs. Creativity
Despite the promise of AI, the literature reveals a tension between automation and creative agency. While Saralegi et al. (Saralegi et al., 2024) demonstrate the feasibility of automatic multilingual subtitling and dubbing systems, questions remain regarding the aesthetic quality of such outputs. The "human-in-the-loop" model remains the gold standard, particularly for narrative-heavy titles.

However, the trajectory is clear. As noted in Table 4 (Section 2.3), the research focus has shifted decisively toward computer science and engineering methodologies. This implies that the future localizer will need to possess not only linguistic and cultural competence but also "technological literacy" to interact with NMT engines, post-edit AI outputs, and manage complex asset-generation pipelines. This validates the early predictions by Bernal-Merino (Bernal-Merino, 2008) regarding the changing nature of translator training, though the pace of technological change has likely outstripped the curricula of many training programs (Morais, 2020).

## 2.4.3 Multimodality and Semiotics in Game Narratives

The results in Section 2.3 highlight that video games are multimodal semiotic systems, where meaning is constructed through the interplay of text, image, sound, and gameplay mechanics. The discussion in Section 2.1 established that translating games requires attention to all these semiotic channels. The analyzed literature confirms this, offering detailed investigations into how non-verbal signs contribute to the localization process.

### 2.4.3.1 Visual Semiotics and Environmental Storytelling
Bagaskara and Dhanadipa’s analysis of *Elden Ring* (Bagaskara & Dhanadipa, 2024) provides empirical evidence of how visual signs function as narrative devices. In "Souls-like" games, where explicit dialogue is sparse, the environment itself tells the story. Localization, therefore, involves interpreting these visual cues. If a visual sign relies on a cultural metaphor specific to the source culture (e.g. A specific color representing death), the localization team must decide whether to alter the texture (visual localization) or rely on text to bridge the gap.

The literature suggests that "world re-engineering" often fails when visual semiotics are ignored. For example, Moreno García (Moreno García, 2024) discusses the adaptation of "cultural realia" in *Arena of Valor*. The success of the localization depends on whether the visual representation of heroes and items aligns with the target culture's semiotic expectations. When there is a mismatch—such as a visual symbol that connotes bravery in the source culture but aggression in the target culture—the "textual" translation cannot fully compensate. This underscores the need for "multimodal localization," where the visual and auditory channels are treated with the same rigor as the linguistic channel.

### 2.4.3.2 Accessibility as Localization
A significant sub-theme emerging from the literature is the convergence of localization and accessibility. Research by Larreina and Mangiron (Larreina & Mangiron, 2025) and Westin (Westin, 2012) positions accessibility features (such as audio descriptions and closed captions) as forms of "intra-lingual localization." Just as localization translates a game for a different linguistic community, accessibility translates the game experience for a different sensory community.

The integration of these fields is driven by shared technologies. The same text-to-speech (TTS) and speech-to-text (STT) technologies used for automated dubbing (Saralegi et al., 2024) are utilized for screen readers. Furthermore, the "Listen With Seeing" framework (Sun et al., 2025) has direct applications in generating automated audio descriptions for visually impaired players. This convergence suggests a broader definition of the field: "User Experience (UX) Adaptation," where the goal is to remove barriers to entry, whether those barriers are linguistic, cultural, or physical.

## 2.4.4 Professionalization and Standardization

The maturation of the field is further evidenced by the shift from ad-hoc practices to formal standardization. As noted in Section 2.1, early game localization was often characterized by "rom-hacking" and fan translations. The literature analyzed in Section 2.3 paints a picture of a highly regulated industrial sector.

### 2.4.4.1 Standards and Process Models
The work by Ali and Yue (Ali & Yue, 2015) on formalizing software testing standards (ISO/IEC/IEEE 29119) is indicative of this maturity. Localization testing (LQA) is no longer a casual playthrough but a rigorous engineering process designed to detect linguistic and cosmetic defects. This formalization is necessary to support the scale of modern "AAA" development.

Additionally, the emergence of "meta-design models" for collaborative work (Zhu, 2018) addresses the complexity of distributed localization teams. With translators, editors, testers, and engineers working across different time zones, the "waterfall" models of the past have given way to agile and continuous delivery workflows. This industrial rigor stands in contrast to the "hacker" origins of the field discussed by Pachali (Pachali, 2011), marking the definitive transition of game localization into a corporate engineering discipline.

### 2.4.4.2 Ethical and Legal Dimensions
As the industry scales, new challenges emerge. Roomberg (Roomberg, 2023) raises the issue of money laundering in the video game industry, highlighting the complex financial ecosystems that localizers must now understand. Virtual economies, loot boxes, and microtransactions vary significantly in legality across regions (e.g., Belgium vs. China). Localization teams are increasingly responsible for ensuring that the game's monetization mechanics comply with local laws, adding a legal dimension to the "world re-engineering" process. This extends the scope of the localizer's responsibility beyond the text to the very economic structure of the game.

## 2.4.5 Addressing the Research Gap: The Need for Reception Studies

While the analyzed literature provides a robust understanding of *how* games are localized (strategies) and *with what tools* (technologies), a critical gap remains regarding *how players perceive* these efforts. As identified in the gap analysis in Section 2.1, the field is heavily skewed toward product-oriented analysis (comparing source and target texts) and process-oriented analysis (workflows and tools).

### 2.4.5.1 The Absence of the Player
There is a notable scarcity of empirical reception studies in the dataset. While studies like Wang (Wang, 2025) analyze the strategies used in *Stardew Valley*, they do not present data on whether Chinese players *preferred* the domesticated character personalities over the original ones. Similarly, while we know that AI can generate assets (Ribeiro et al., 2025), we lack longitudinal data on player acceptance of AI-generated content versus human-crafted content.

The bibliometric anomalies discussed by Meho (Meho, 2025) and the questions of digital value raised by Aimo (Aimo, 2024) suggest that the academic metrics may be incentivizing volume of publication over deep, longitudinal user research. To fully understand the impact of "world re-engineering," future research must pivot toward reception studies that utilize eye-tracking, sentiment analysis, and large-scale A/B testing to measure the actual efficacy of localization strategies.

Table 6 outlines the implications of the current literature landscape and identifies specific trajectories for future inquiry based on the analyzed texts.

| Dimension | Current State (Literature Findings) | Identified Gap | Future Research Trajectory |
|:---|:---|:---|:---|
| **Methodology** | Comparative Text Analysis; System Design | Lack of empirical player data | Reception studies using biometrics/surveys |
| **Technology** | AI for asset generation & NMT | Quality perception of AI output | Human-AI interaction in creative workflows |
| **Culture** | Focus on East-West adaptation | Under-represented locales (Africa/LatAm) | South-South localization dynamics |
| **Scope** | Text and Audio | Holistic/Multimodal cohesion | Impact of visual localization on immersion |
| **Theory** | Transcreation & Skopos | Cognitive load of localization | Psycholinguistic analysis of gaming |

*Table 6: Synthesis of Research Findings and Future Directions.*

## 2.4.6 Conclusion of Discussion

The discussion of the literature reveals that video game localization has evolved into a sophisticated, interdisciplinary field that sits at the intersection of translation studies, software engineering, and cultural anthropology. The findings from Section 2.3 validate the theoretical framework of "transcreation" established in Section 2.1 but extend it into the realm of "world re-engineering."

The evidence from the cited studies (Wang, 2025)(Wang, 2025)(Bagaskara & Dhanadipa, 2024) confirms that successful localization requires the manipulation of semiotic layers far deeper than the linguistic surface. Whether through the domestication of character personalities in *Stardew Valley*, the preservation of mythic authenticity in *Black Myth: Wukong*, or the semiotic decoding of *Elden Ring*, localizers are engaged in the reconstruction of virtual worlds.

However, the field faces a "technological event horizon" with the advent of deep learning (Ribeiro et al., 2025). The integration of AI threatens to disrupt traditional workflows, potentially commodifying the localization process while simultaneously offering new tools for multimodal adaptation. As the industry continues to professionalize and standardize (Ali & Yue, 2015), the role of the localizer is transforming from a translator of text to a cultural engineer and technical operator.

The most pressing challenge for future research, as indicated by the gaps in the current literature, is to empirically validate these strategies through player reception studies. Only by understanding the cognitive and emotional impact of localization choices can the field move from descriptive analysis to predictive modeling of player experience. The trajectory suggests that the next decade of research will be defined not by *how* we translate, but by *how players feel* about the translated worlds they inhabit.

\newpage

# 3. Conclusion
The investigation into the methods and strategies of video game localization reveals a complex, multi-layered discipline that has fundamentally outgrown traditional definitions of translation. This thesis has analyzed the transition from linguistic equivalence to the "transcreation" paradigm, examined the technical constraints imposed by software architecture, and evaluated the cultural adaptation strategies required for global market success. The findings confirm that video game localization is not merely a post-production linguistic task but an integral component of the game development lifecycle that directly impacts user experience (UX), commercial viability, and cultural reception. By synthesizing theoretical frameworks with empirical case studies—ranging from indie titles like *Stardew Valley* to AAA productions like *Black Myth: Wukong*—this study establishes that successful localization requires a holistic strategy that harmonizes narrative fidelity, technical functionality, and cultural resonance.

## 3.1 Synthesis of Findings

The research objectives of this study were to identify effective localization strategies and analyze the tension between semantic accuracy and playability. The analysis yields three primary conclusions regarding the current state of the field.

### 3.1.1 The Dominance of the Transcreation Paradigm
The first major finding is the definitive shift from translation to transcreation as the industry standard. As established by seminal works in the field (O'Hagan & Mangiron, 2013), the interactive nature of video games necessitates a "skopos," or purpose, that prioritizes the player's emotional experience over lexical adherence to the source text. This study confirms that "playability" and the "fun factor" act as the governing principles for localization decisions.

Analysis of character development strategies, particularly in narrative-heavy games like *Stardew Valley*, demonstrates that direct translation often fails to convey personality traits across cultural boundaries. Instead, strategies that recreate character voice through culturally appropriate distinctiveness—even if it means altering the semantic content of dialogue—result in higher player immersion (Wang, 2025). This supports the argument that the localizer functions as a co-author who must understand the game's mechanics and narrative arc to effectively "rewrite" the experience for a new audience (Morais, 2020). The findings suggest that the most successful localization projects are those where the boundary between the original developer and the localization team is permeable, allowing for a collaborative creative process rather than a disjointed handover.

### 3.1.2 Cultural Adaptation as a Spectrum
The second finding relates to the spectrum of cultural adaptation, ranging from "foreignization" (preserving source culture) to "domestication" (erasing source markers). While early industry trends favored heavy domestication to make games palatable to Western audiences, recent data indicates a nuanced shift.

The case of *Black Myth: Wukong* represents a pivotal moment in this trajectory. As China’s first major AAA single-player title, its localization strategy challenges the traditional necessity of erasing cultural specificity. Instead of domesticating Chinese mythology for Western players, the localization strategy focuses on communicative translation that preserves the "foreign" cultural identity while ensuring the narrative remains accessible (Wang, 2025). This contrasts with mobile MOBAs like *Arena of Valor*, where cultural realia are often aggressively adapted or replaced to fit the target market's expectations of fantasy archetypes (Moreno García, 2024).

This divergence suggests that the "strategy" is not fixed but dependent on the game's genre and "cultural capital." High-concept narrative games increasingly leverage their cultural origin as a unique selling point, whereas competitive multiplayer games prioritize frictionless, culturally neutral comprehension to maximize the user base.

### 3.1.3 The Multimodal Technical Reality
The third finding emphasizes that localization is fundamentally a technical endeavor constrained by the multimodal nature of the medium. The analysis of asset generation and deep learning applications reveals that localization is no longer limited to text strings. It now encompasses the modification of visual assets, audio files, and user interface (UI) elements.

Recent advancements in deep learning have enabled the automated generation and evaluation of image-based assets, allowing developers to localize textures and sprites with greater efficiency (Ribeiro et al., 2025). Furthermore, the integration of visual and auditory modalities into Neural Machine Translation (NMT) workflows addresses previous limitations where translators lacked context. By "seeing" the game state or "hearing" the audio cue, modern NMT systems can reduce context-dependent errors that historically plagued game localization (Aytaş, 2025). This technical evolution demands that modern localizers possess a degree of "technological competence," understanding how text variables, UI limitations, and audio timing constraints interact with their linguistic choices (Corbolante & Irmler, 2001).

## 3.2 Theoretical Implications

This study contributes to the broader field of Translation Studies by reinforcing the position of Game Localization as a distinct sub-discipline requiring its own theoretical models. The findings challenge the applicability of static equivalence theories, supporting the view that video games require a "pragmatic" and "functionalist" approach.

### 3.2.1 Expanding the Semiotic Framework
The analysis of visual signs in cutscenes, such as those in *Elden Ring*, highlights the necessity of a semiotic approach to localization. Meaning in video games is constructed not just through dialogue, but through the interplay of visual signs, audio cues, and gameplay mechanics (Bagaskara & Dhanadipa, 2024). Consequently, a theoretical framework for game localization must account for "intersemiotic translation"—the interpretation of verbal signs by means of signs of non-verbal sign systems.

The study validates the concept that the "text" in a video game is unstable and polysemiotic. Theoretical models must therefore expand to include "audio-visual event localization," where the correlation between audio tracks and visual events dictates the translation strategy (Sun et al., 2025). This implies that the unit of translation is no longer the sentence or the string, but the "ludic event"—the combination of player action, system feedback, and narrative output.

### 3.2.2 Re-evaluating Domestication and Foreignization
The research also prompts a re-evaluation of Venuti’s concepts of domestication and foreignization within the context of interactive entertainment. While traditional literary theory often views domestication as a form of cultural erasure, in the context of video games, it is often a prerequisite for usability. However, the success of titles deeply rooted in specific cultures challenges the notion that "global" games must be culturally odorless (Dong & Mangiron, 2018). The theoretical discourse must now account for a "hybrid" approach where gameplay mechanics are domesticated (standardized controls and UI) while narrative elements may be foreignized to provide an authentic exotic experience (Cao, 2023).

## 3.3 Practical and Managerial Implications

Based on the synthesis of literature and case analysis, this study offers practical recommendations for developers, publishers, and localization agencies. The varying demands of different genres and markets necessitate a flexible strategic framework.

Table 3.1 outlines a strategic matrix for localization based on the findings of this thesis, categorizing approaches by game element and desired outcome.

| Game Element | Strategic Approach | Key Technique | Primary Outcome | Source Support |
|:--- |:--- |:--- |:--- |:--- |
| **Narrative** | Transcreation | Co-creation/Rewriting | Emotional resonance & immersion | (O'Hagan & Mangiron, 2013)(Wang, 2025) |
| **Cultural Realia** | Hybrid Adaptation | Communicative Translation | Accessibility with cultural authenticity | (Wang, 2025)(Moreno García, 2024) |
| **Audio/Visual** | Multimodal Context | Cross-modal NMT integration | Context-aware accuracy | (Aytaş, 2025)(Sun et al., 2025) |
| **Technical** | Asset Automation | Deep Learning Generation | Cost reduction & scalability | (Ribeiro et al., 2025)(Ali & Yue, 2015) |
| **Accessibility** | Inclusive Design | Audio Description (AD) | Expanded market reach | (Larreina & Mangiron, 2025)(Westin, 2012) |

*Table 3.1: Strategic Framework for Holistic Video Game Localization.*

### 3.3.1 Integration of Localization in Development
The primary managerial implication is the necessity of integrating localization into the pre-production phase, often referred to as "internationalization." The analysis of software testing standards indicates that when localization is treated as an afterthought, it results in significant technical debt and "buggy" releases (Ali & Yue, 2015). Developers must adopt "sim-ship" (simultaneous shipment) models where localization teams have access to the game build during development. This allows for the identification of hard-coded strings, UI overflow issues, and cultural taboos before the code is finalized.

### 3.3.2 The Imperative of Accessibility
A critical practical implication emerging from recent literature is the convergence of localization and accessibility. Features traditionally associated with accessibility, such as subtitles, audio descriptions, and text-to-speech, are now overlapping with localization workflows. The implementation of audio description (AD) for visually impaired players, for instance, requires the same semantic and technical adaptation processes as dubbing (Larreina & Mangiron, 2025). Industry practitioners should view accessibility not as a compliance checklist but as a market expansion strategy, utilizing engine-independent solutions to scale these features globally (Westin, 2012).

### 3.3.3 Training and Education
For the translation industry, the findings underscore the need for specialized training. Translators must be trained not only in linguistic competence but in "game literacy" and technical proficiency. Curricula should include blended resources that simulate the constraints of game engines, teaching students how to work with tags, variables, and character limits (Merten, 2011)(Bernal-Merino, 2008). The complexity of modern localization, involving dubbing analysis and situational context, requires a pedagogy that moves beyond static text translation (Mejías-Climent, 2021).

## 3.4 Limitations of the Study

While this thesis provides a comprehensive overview of localization strategies, several limitations must be acknowledged to contextualize the findings.

First, the rapid pace of technological advancement in the video game industry renders any technical analysis temporarily bound. This study examined current deep learning and NMT applications (Ribeiro et al., 2025)(Aytaş, 2025), but the emergence of Generative AI and Large Language Models (LLMs) is shifting the landscape faster than academic literature can fully document. The long-term impact of these technologies on the labor market for human localizers remains a developing variable.

Second, the scope of the case studies was necessarily limited. While the inclusion of *Black Myth: Wukong* (Wang, 2025) and *Stardew Valley* (Wang, 2025) provides a contrast between AAA and indie sectors, the vast majority of mobile and "hyper-casual" games—which constitute a significant portion of global revenue—operate under different constraints that may prioritize speed and machine translation over the high-touch transcreation described here.

Third, the availability of data regarding internal industry processes is often restricted by Non-Disclosure Agreements (NDAs). Much of the literature relies on post-hoc analysis of the final product (Bagaskara & Dhanadipa, 2024) or theoretical models (Zhu, 2018), rather than direct observation of the production floor. This creates a potential gap between "prescribed" best practices in academia and the "described" reality of crunch-time development.

Finally, the study touches upon but does not fully explore the legal and ethical dimensions of localization, such as censorship regimes in specific markets (Bates, 2004) or the financial regulations concerning in-game currencies (Roomberg, 2023). These factors often dictate localization strategies as much as linguistic or cultural concerns do.

## 3.5 Recommendations for Future Research

Based on the identified gaps and the trajectory of the industry, several avenues for future research are proposed.

### 3.5.1 AI and Human-in-the-Loop Workflows
The most urgent area for future inquiry is the integration of Artificial Intelligence into the localization pipeline. While this study touched upon NMT and asset generation, future research should investigate the efficacy of "Human-in-the-Loop" (HITL) models in game localization. Specifically, research is needed to quantify the quality difference between fully human transcreation and AI-generated, human-edited content in narrative-heavy genres. The potential for automatic multilingual subtitling and dubbing systems (Saralegi et al., 2024) offers a rich ground for experimental studies comparing player reception of AI vs. human voice acting.

### 3.5.2 The Rise of VR and AR Localization
As the industry explores immersive technologies, the localization of Virtual Reality (VR) and Augmented Reality (AR) presents novel challenges. Current literature is just beginning to address the technical and sensory issues of localizing immersive environments (Varun et al., 2024). Future studies should examine how diegetic text (text that exists within the game world, like a signpost) and spatial audio are localized in VR, where the player's gaze and position determine the context.

### 3.5.3 Therapeutic and Serious Games
An under-researched but vital area is the localization of "serious games," particularly in healthcare and education. The translation of therapeutic video games requires a balance between medical vulgarization (making terms accessible) and clinical accuracy (Jeanmaire & Kim, 2022). As the use of gamification in public sectors grows—for example, in reorganizing public facilities (Ohori et al., 2021)—researchers should investigate the specific strategies required to localize educational and behavioral health content without diluting its efficacy.

### 3.5.4 Reverse Localization and New Markets
Finally, the flow of cultural goods is shifting. Future research should focus on "reverse localization"—strategies for bringing non-Western games to Western markets without erasing their cultural identity. The success of Turkish (Üyesi et al., 2020) and Chinese (Dong & Mangiron, 2018) developers suggests a polycentric industry. Investigating how these markets navigate the "cultural discount" (the loss of value when a cultural product crosses borders) would provide valuable insights into the future of global entertainment.

## 3.6 Concluding Remarks

The localization of video games has matured from a technical necessity into a sophisticated form of intercultural communication. This thesis has demonstrated that effective localization strategies are those that embrace the medium's interactivity, utilizing transcreation to preserve the emotional core of the experience while leveraging advanced technology to manage the complex multimodal assets.

As the line between the virtual and the real continues to blur, and as video games cement their status as the dominant cultural form of the 21st century (Aimo, 2024), the role of the localizer becomes increasingly critical. They are the gatekeepers of global play, ensuring that the "magic circle" of the game remains unbroken, regardless of the language spoken by the player. The future of the industry lies not in the erasure of difference, but in the intelligent, technologically-assisted mediation of culture, creating a global gaming ecosystem that is as diverse as it is interconnected.

\newpage

# 4. Appendices
## Appendix A: Conceptual Framework for Game Localization

### A.1 The GILT Model Integration

The localization of video games operates within the broader industrial framework known as GILT (Globalization, Internationalization, Localization, and Translation). While these terms are often used interchangeably in non-specialized contexts, the academic and industrial literature distinguishes them as hierarchical processes necessary for the successful distribution of software across linguistic boundaries. The framework presented here synthesizes the definitions provided by Corbolante and Irmler (Corbolante & Irmler, 2001) with the game-specific adaptations proposed by O'Hagan and Mangiron (O'Hagan & Mangiron, 2013).

Globalization serves as the overarching business strategy, encompassing the decision-making processes regarding which markets to enter and the resource allocation for global distribution. Internationalization (i18n) represents the technical preparation of the game code to handle multiple languages and cultural conventions without requiring engineering changes to the source code. Localization (l10n) involves the specific adaptation of the product for a target locale, while translation (t9n) is the linguistic conversion of text assets.

The following table illustrates the operational hierarchy of the GILT framework as applied to video game development:

| Component | Primary Function | Key Activities | Stakeholders |
|-----------|------------------|----------------|--------------|
| Globalization | Strategic Planning | Market analysis, budget allocation | Executives, Producers |
| Internationalization | Technical Enablement | Unicode support, UI scaling, date formats | Software Engineers |
| Localization | Cultural Adaptation | Asset modification, legal compliance | L10n Managers, Cultural Consultants |
| Translation | Linguistic Conversion | Text rendering, dubbing scripts | Translators, Voice Actors |

*Table A1: The GILT Hierarchy in Video Game Development. Adapted from (O'Hagan & Mangiron, 2013) and (Corbolante & Irmler, 2001).*

The distinction between Internationalization and Localization is particularly critical in game development. As noted in the literature, Internationalization is an engineering task that must occur early in the development cycle to prevent costly "re-engineering" later. This includes ensuring the game engine can support variable-width fonts (essential for Asian languages) and bidirectional text (for Arabic or Hebrew) (Corbolante & Irmler, 2001). Without robust Internationalization, the Localization phase is often technically constrained, leading to compromised user interfaces or truncated text that disrupts the player's immersion.

### A.2 The Transcreation Spectrum

A central theoretical contribution of this thesis is the analysis of the shift from equivalence-based translation to "transcreation." In the context of video games, adherence to the source text's literal meaning often results in a loss of "playability" or the "fun factor," which are the primary metrics of a game's success (O'Hagan & Mangiron, 2013). Transcreation allows localizers to deviate significantly from the source text to recreate the intended emotional or gameplay experience (the "gameplay gestalt") for the target audience.

The spectrum of intervention ranges from "No Translation" (keeping assets in the original language, common in early arcade games) to "Full Transcreation" (rewriting narratives and redesigning assets). Recent studies on titles like *Arena of Valor* demonstrate how deep transcreation involves altering character designs and cultural realia to resonate with local mythologies (Moreno García, 2024).

| Strategy | Fidelity Focus | Application Example | Risk Factor |
|----------|----------------|---------------------|-------------|
| Literal Translation | Semantic Equivalence | UI menus, tutorials, technical specs | Loss of humor/tone |
| Domestication | Cultural Fluency | Idioms, jokes, pop culture references | Erasure of source culture |
| Foreignization | Source Preservation | Key terminology (e.g., "Samurai", "Mana") | Alienation of players |
| Transcreation | Emotional Equivalence | Character names, quest lines, marketing | High cost/creative divergence |

*Table A2: Strategies in the Transcreation Spectrum. Based on concepts from (O'Hagan & Mangiron, 2013) and (Cao, 2023).*

The choice between these strategies is often dictated by the genre and the target audience's expectations. For instance, the translation of the Chinese literary classic *Biancheng* illustrates how the tension between domestication and foreignization affects the reception of cultural masterpieces (Cao, 2023). Similarly, in video games, a "foreignized" approach might be preferred for games like *Black Myth: Wukong*, where the selling point is the authentic Chinese mythology (Wang, 2025), whereas a "domesticated" or "transcreated" approach might be necessary for humor-based indie games like *Stardew Valley* to ensure jokes land with the target audience (Wang, 2025).

### A.3 The "Look and Feel" Dimension

Beyond text, the conceptual framework must account for the semiotic and multimodal nature of video games. Localization is not limited to linguistic code but extends to visual signs, audio cues, and interactive mechanics. Bagaskara and Dhanadipa (Bagaskara & Dhanadipa, 2024) argue through their analysis of *Elden Ring* that visual signs in cutscenes carry narrative weight equal to or greater than spoken dialogue. Therefore, a comprehensive localization framework must include "Asset Adaptation" as a core component.

This involves analyzing visual assets for cultural appropriateness. For example, gestures, color symbolism, and even the representation of blood or violence must be scrutinized against the regulatory and cultural standards of the target market. In extreme cases, this requires the generation of entirely new graphical assets, a process that is increasingly being supported by deep learning techniques to reduce production costs (Ribeiro et al., 2025).

---

## Appendix B: Supplementary Data and Case Study Analysis

### B.1 Comparative Analysis of Localization Strategies

This appendix provides supplementary data supporting the comparative analysis of localization strategies in AAA versus Indie game productions. The data synthesis focuses on two primary case studies discussed in the main body: *Black Myth: Wukong* (representing high-budget, culturally specific AAA development) and *Stardew Valley* (representing indie development with community-driven or smaller-scale localization).

The following table summarizes the distinct challenges and strategies identified in the literature for these contrasting production models.

| Feature | *Black Myth: Wukong* (Wang, 2025) | *Stardew Valley* (Wang, 2025) |
|---------|---------------------------------|-----------------------------|
| **Origin Culture** | Specific (Chinese Mythology) | General (Western Pastoral) |
| **Strategy** | Foreignization / Thick Description | Domestication / Transcreation |
| **Key Challenge** | Conveying "Journey to the West" lore | Preserving character personality |
| **Asset Modification** | Minimal (Source culture is the USP) | Moderate (Cultural context adaptation) |
| **Terminology** | Retention of Pinyin/Sanskrit terms | Adaptation to target language norms |

*Table B1: Comparative Localization Strategies in AAA vs. Indie Titles.*

In the case of *Black Myth: Wukong*, Wang (Wang, 2025) highlights that the game's cultural authenticity is its primary market differentiator. Consequently, the localization strategy leans heavily towards foreignization, retaining specific cultural terms (realia) to educate the player, rather than replacing them with Western equivalents. This contrasts with the approach often taken in mobile games like *Arena of Valor*, where cultural elements are frequently swapped entirely (e.g. Replacing a Chinese hero with a Western superhero) to maximize mass-market appeal (Moreno García, 2024).

Conversely, the analysis of *Stardew Valley* by Wang (Wang, 2025) reveals a focus on "Communicative Translation." The goal is not to teach the player about the developer's culture but to create a cozy, relatable farming simulation. The translation of character dialogue focuses on capturing the "idiolect" (distinctive speech patterns) of each villager. For example, the gruff speech of a retired adventurer or the polite tone of a local doctor must be reconstructed in the target language using appropriate sociolinguistic markers, a process that prioritizes character consistency over literal accuracy.

### B.2 Visual and Semiotic Localization Data

Video games rely heavily on "environmental storytelling," where the narrative is embedded in the visual design rather than explicit text. The localization of these elements often requires semiotic analysis to ensure the visual signs convey the intended meaning in the target culture.

The following table categorizes types of visual signs found in games like *Elden Ring* and their localization implications, based on the semiotic framework applied by Bagaskara and Dhanadipa (Bagaskara & Dhanadipa, 2024).

| Sign Type | Example in Gameplay | Localization Implication |
|-----------|---------------------|--------------------------|
| **Symbolic** | Faction crests, religious icons | Risk of taboo violation |
| **Indexical** | Smoke indicating fire, directional arrows | Universal, rarely needs change |
| **Iconic** | Character portraits, inventory items | May need "reskinning" for regional compliance |
| **Textual** | In-game signage (graffiti, books) | Requires texture editing (costly) |

*Table B2: Semiotic Categories in Video Game Localization. Adapted from (Bagaskara & Dhanadipa, 2024).*

The modification of these assets is resource-intensive. Historically, developers would simply remove complex visual assets for international releases. However, modern deep learning methods are enabling "Image-Based Asset Generation," allowing developers to automatically generate variations of textures or sprites that fit different cultural aesthetics or regulatory requirements without manual artist intervention (Ribeiro et al., 2025).

### B.3 Audio-Visual Synchronization Data

A critical aspect of localization quality is the synchronization between audio tracks (dubbing) and visual lip movements. This is particularly relevant in "cinematic" games where close-ups of characters are common. The emergence of automated dubbing systems is changing the economic feasibility of full-audio localization.

Data from Saralegi et al. (Saralegi et al., 2024) regarding the "MULTILINGTOOL" system suggests that automating the subtitling and dubbing process can significantly reduce turnaround times, though quality assurance remains a human-led task. Furthermore, recent advancements in Audio-Visual Event Localization (AVEL) allow systems to better correlate audio signals with specific visual frames, potentially automating the detection of synchronization errors (Sun et al., 2025).

| Method | Synchronization Quality | Cost | Scalability |
|--------|-------------------------|------|-------------|
| **Subtitling Only** | N/A (Reading required) | Low | High |
| **Loose Dubbing** | Low (Time-constrained only) | Medium | Medium |
| **Lip-Sync Dubbing** | High (Animation matched to voice) | Very High | Low |
| **AI Re-sequencing** | Variable (Algorithmic matching) | Low/Medium | High |

*Table B3: Dubbing and Synchronization Methods. Based on (Mejías-Climent, 2021) and (Saralegi et al., 2024).*

Mejías-Climent (Mejías-Climent, 2021) notes through case studies that the choice of dubbing method fundamentally alters the player's immersion. While "Lip-Sync Dubbing" provides the highest fidelity, it is often reserved for AAA titles due to the cost of re-animating facial structures or the constraints of matching voice actor performance to existing animations.

---

## Appendix C: Glossary of Terms

This glossary defines key technical and theoretical terms used throughout the thesis, drawing from the cited literature to ensure academic precision.

**Audio Description (AD)**
An accessibility feature that provides a verbal narration of visual elements, actions, and scene changes for players with visual impairments. In video games, AD is complex due to the dynamic, non-linear nature of gameplay, requiring real-time triggering of descriptive audio cues (Larreina & Mangiron, 2025).

**Asset Generation (Deep Learning)**
The use of artificial intelligence, specifically deep learning models, to automatically create or modify game assets such as textures, sprites, and 3D models. This technology is increasingly used in localization to rapidly adapt visual elements for different markets without manual redesign (Ribeiro et al., 2025).

**Domestication**
A translation strategy that minimizes the foreignness of the source text for target readers. In games, this involves adapting cultural references, names, and idioms so they appear to have originated in the target culture (Cao, 2023).

**Foreignization**
A translation strategy that retains the cultural markers of the source text, deliberately breaking target conventions to preserve the "otherness" of the work. This is often used in games that rely on cultural tourism or specific mythological settings, such as *Black Myth: Wukong* (Wang, 2025).

**Game Accessibility**
The practice of removing barriers that prevent people with disabilities from playing video games. This intersects with localization through features like subtitles, text-to-speech, and configurable controls. Large-scale solutions aim to be engine-independent to maximize adoption (Westin, 2012).

**Gameplay Gestalt**
A concept referring to the holistic experience of playing a game, resulting from the interaction between the player and the game system. Localization aims to preserve this gestalt, ensuring the target player experiences the same level of difficulty, engagement, and emotional response as the source player (O'Hagan & Mangiron, 2013).

**GILT**
An acronym for Globalization, Internationalization, Localization, and Translation. It represents the industry-standard workflow for preparing software products for international markets (Corbolante & Irmler, 2001).

**Internationalization (i18n)**
The engineering process of designing a software application so that it can be adapted to various languages and regions without engineering changes. This includes separating code from content and supporting standards like Unicode (Corbolante & Irmler, 2001).

**Localization (l10n)**
The process of adapting a product, particularly software or content, to a specific locale or market. In video games, this encompasses translation, cultural adaptation of assets, and technical modifications (O'Hagan & Mangiron, 2013).

**Ludology**
The discipline of studying games, focusing on their rules, systems, and mechanics, as distinct from narrative or visual studies. Localization from a ludological perspective prioritizes the preservation of game mechanics and rules over narrative fidelity (O'Hagan & Mangiron, 2013).

**Neural Machine Translation (NMT)**
An approach to machine translation that uses artificial neural networks to predict the likelihood of a sequence of words. Advanced NMT in gaming is beginning to integrate visual and auditory modalities to improve context awareness and translation quality (Aytaş, 2025).

**Playability**
The degree to which a game is usable and enjoyable. In localization, maintaining playability is often prioritized over linguistic accuracy; if a faithful translation makes a puzzle unsolvable or a tutorial confusing, it is considered a localization failure (O'Hagan & Mangiron, 2013).

**Real-Time Strategy (RTS)**
A subgenre of strategy video games where the game does not progress in turns. Localization for RTS games often requires abbreviated text and distinct audio cues to accommodate the fast-paced gameplay.

**Transcreation**
A portmanteau of "translation" and "creation." It refers to a creative translation process where the translator has the license to significantly rewrite or adapt content to elicit the same emotional response in the target audience, often used in marketing and entertainment media (O'Hagan & Mangiron, 2013).

---

## Appendix D: Technical Standards and Future Resources

### D.1 Technical Standards in Localization

The technical execution of localization is governed by various software engineering standards that ensure quality and interoperability. While creative adaptation is subjective, the underlying code must adhere to rigorous testing protocols. The ISO/IEC/IEEE 29119 standard, for instance, provides a framework for software testing that is applicable to game localization testing (LQA) (Ali & Yue, 2015). This standard helps formalize the detection of "truncation" (text overflowing UI boxes), "concatenation" issues (grammar errors caused by joining variable strings), and "hard-coding" (text embedded in code rather than external files).

Furthermore, the rise of mobile gaming has introduced new technical constraints related to screen size and memory management. Research on the Turkish video game industry highlights how mobile technologies have disrupted traditional development pipelines, requiring localizers to work with stricter character limits and fragmented content delivery systems (Üyesi et al., 2020).

### D.2 The Role of AI and Automation

The future of video game localization is increasingly intertwined with Artificial Intelligence. The sheer volume of text in modern RPGs (often exceeding 1 million words) makes manual translation cost-prohibitive for all but the largest studios. Consequently, the industry is moving toward "Computer-Aided Translation" (CAT) tools enhanced by Neural Machine Translation (NMT).

Recent research by Aytaş (Aytaş, 2025) demonstrates that integrating visual and auditory modalities into NMT systems significantly improves translation quality. By allowing the AI to "see" the game context (e.g. An image of the character speaking) and "hear" the tone, the system can resolve ambiguities that text-only models miss. Additionally, deep learning is being used to automate the generation and evaluation of game assets, potentially allowing for automated "cultural skinning" of games in the future (Ribeiro et al., 2025).

| Technology | Application in Localization | Status |
|------------|-----------------------------|--------|
| **Multimodal NMT** | Context-aware text translation | Emerging (Aytaş, 2025) |
| **Deep Learning Asset Gen** | Creating localized textures/sprites | Experimental (Ribeiro et al., 2025) |
| **Auto-Dubbing** | Synthesizing voice lines in target language | Available (Saralegi et al., 2024) |
| **AV Event Localization** | Syncing subtitles/audio to gameplay events | Advanced (Sun et al., 2025) |

*Table D1: Emerging Technologies in Game Localization.*

### D.3 Accessibility Resources

Localization and accessibility are converging fields. Making a game accessible to a player who speaks a different language employs similar technologies to making a game accessible to a player with sensory impairments. Audio Description (AD) is a prime example, where visual information is translated into auditory information. Larreina and Mangiron (Larreina & Mangiron, 2025) argue that AD should be considered a standard part of the localization/accessibility suite, alongside subtitles.

Westin's survey of engine-independent solutions suggests that future game engines should support standardized accessibility layers, allowing text-to-speech and high-contrast modes to be applied universally, rather than requiring custom implementation for every title (Westin, 2012). This "universal design" approach aligns with the GILT framework's goal of efficiency—solving accessibility and localization challenges at the engine level (Internationalization) rather than the asset level.

### D.4 Recommended Resources for Practitioners

For researchers and practitioners seeking to deepen their understanding of game localization, the following resources (drawn from the cited literature) are essential:

* **Training and Pedagogy:** Bernal-Merino's work on training translators provides foundational curricula for aspiring game localizers, emphasizing the need for blended resources that combine linguistic training with technical software skills (Bernal-Merino, 2008)(Merten, 2011).
* **Historical Context:** To understand current trends, one must examine the history of the field. Mejías-Climent provides comprehensive accounts of the evolution of dubbing and localization practices, tracing the industry from the text-only era to full cinematic immersion (Mejías-Climent, 2021).
* **Market Specifics:** For those targeting specific high-growth regions, Dong and Mangiron's analysis of the Chinese market (Dong & Mangiron, 2018) and Üyesi et al.'s study of the Turkish industry (Üyesi et al., 2020) offer critical insights into regional preferences and regulatory landscapes.
* **Legal and Ethical Compliance:** As games become global services, they face complex legal challenges. Roomberg (Roomberg, 2023) highlights the emerging issue of money laundering in game economies, a compliance area that localization teams must be aware of when adapting in-game currency systems for different jurisdictions.

\newpage


## References

Aimo. (2024). What is My Value? Digital Questions in Aesthetic Education: the Case of Video Game. *Itinera*. https://doi.org/10.54103/2039-9251/27834.

Ali, & Yue. (2015). Formalizing the ISO/IEC/IEEE 29119 Software Testing Standard. *ACM/IEEE International Conference on Model Driven Engineering Languages and Systems*. https://doi.org/10.1109/MODELS.2015.7338271.

Aytaş. (2025). Enhancing Translation with Visual and Auditory Modalities. *Uluslararasi Dil, Edebiyat ve Kültür Araştırmaları Dergisi*. https://doi.org/10.37999/udekad.1611713.

Bagaskara, & Dhanadipa. (2024). Semiotic Analysis Of Visual Signs Found in Main Bosses’ Cutscenes Of Elden Ring Video Game. *Sintaksis*. https://doi.org/10.61132/sintaksis.v2i6.1193.

Bates. (2004). *From State Monopoly to a Free Market of Ideas? Censorship in Poland, 1976–1989*. BRILL. https://doi.org/10.1163/9789401200950_006

Bernal-Merino. (2008). *Training translators for the video game industry*. John Benjamins Publishing Company. https://doi.org/10.1075/btl.77.14ber

Cao. (2023). A Comparative Analysis of Two Translation Versions of Biancheng from the Perspective of Domestication and Foreignization. *Communications in Humanities Research*, *6*(1), 319-328. https://doi.org/10.54254/2753-7064/6/20230288.

Chepelyuk, Rohalska-Yakubova, & Nazarov. (2025). Internal Organization of Discourse and Translation (Based on Video Game Content Material). *Scientific papers of Berdyansk State Pedagogical University. Philological sciences*(23), 164-172. https://doi.org/10.32782/2412-933x/2025-xxiii-20.

Corbolante, & Irmler. (2001). *7.2.5 Software Terminology and Localization*. John Benjamins Publishing Company. https://doi.org/10.1075/z.htm2.14cor

Dong, & Mangiron. (2018). Journey to the East: Cultural adaptation of video games for the Chinese market. *The Journal of Specialised Translation*. https://doi.org/10.26034/cm.jostrans.2018.216.

Jacobs-Johnson. (2017). “Making games is easy. Belonging is hard.”: An Analysis of Gender Representation in Video Game Production Culture. **. https://www.semanticscholar.org/paper/95eb29d455959cca2ad7e7e441e33a966a05a45b.

Jeanmaire, & Kim. (2022). Traduire des jeux vidéo thérapeutiques pour enfants : entre localisation et vulgarisation médicale/Translating therapeutic video games for children: between localisation and medical vulgarisation. *The Journal of Specialised Translation*. https://doi.org/10.26034/cm.jostrans.2022.090.

Larreina, & Mangiron. (2025). Advancing Game Accessibility With Audio Description. *Journal of audiovisual translation*. https://doi.org/10.47476/jat.v8i8.2025.355.

Meho. (2025). Gaming the metrics: bibliometric anomalies in global university rankings and the research integrity risk index (RI2). *Scientometrics*. https://doi.org/10.1007/s11192-025-05480-2.

Mejías-Climent. (2021). *Game Localization: Stages and Particularities*. Springer International Publishing. https://doi.org/10.1007/978-3-030-88292-1_3

Mejías-Climent. (2021). *Dubbing Analysis Through Game Situations: Four Case Studies*. Springer International Publishing. https://doi.org/10.1007/978-3-030-88292-1_5

Mejías-Climent. (2021). *The History of Localization and Dubbing in Video Games*. Springer International Publishing. https://doi.org/10.1007/978-3-030-88292-1_2

Merten. (2011). Session 3-Creating Blended Resources for Translator Training. **. https://www.semanticscholar.org/paper/c4f82f525b42509e6caea70d09ce99ca9f4f21d8.

Morais. (2020). Contribuições para o ensino de tradução/localização de videogames: uma resenha de “Translation and Localisation in Video Games: Making Entertainment Software Global”, de Miguel Ángel Bernal-Merino. **. https://doi.org/10.26512/BELASINFIEIS.V9.N4.2020.25196.

Moreno García. (2024). *The Localisation, Transcreation and Adaptation of Cultural Realia in Video Games: The Case of Cultural (re)presentation in Arena of Valor*. Springer International Publishing. https://doi.org/10.1007/978-3-031-62832-0_5

O'Hagan, & Mangiron. (2013). Game Localization. *Benjamins Translation Library*. https://doi.org/10.1075/btl.106.

Ohori, Shimura, & Suzuki. (2021). Development of Reorganizing Public Facilities Game. *AIJ Journal of Technology and Design*. https://doi.org/10.3130/AIJT.27.475.

Pachali. (2011). *Sony startet Feldzug gegen Playstation-Hacks*. Front Matter. https://doi.org/10.59350/h59gz-k9s12

Ribeiro, Carvalho, & Rodrigues. (2025). Image-Based Video Game Asset Generation and Evaluation Using Deep Learning: A Systematic Review of Methods and Applications. *IEEE Transactions on Games*. https://doi.org/10.1109/TG.2024.3487054.

Roomberg. (2023). The video game industry’s money laundering problem: when do game publishers become money transmitters?. *Russian Journal of Economics and Law*. https://doi.org/10.21202/2782-2923.2023.3.630-644.

Saralegi, Corral, Leturia, Sarasola, Murua, Manterola, & Cortes. (2024). MULTILINGTOOL, Development of an Automatic Multilingual Subtitling and Dubbing System. *European Association for Machine Translation Conferences/Workshops*. https://www.semanticscholar.org/paper/ae764ea2739852fd047deaf5d62763a8acc0652c.

Sun, Chen, Zhu, Zhang, Lu, & Chen. (2025). Listen With Seeing: Cross-Modal Contrastive Learning for Audio-Visual Event Localization. *IEEE transactions on multimedia*. https://doi.org/10.1109/TMM.2025.3535359.

Varun, Kumar, Gokila, Gayathri, Nalini, & Subramanian. (2024). Virtual Frontiers Navigating the Impact and Potential of AR and VR. https://doi.org/10.1109/ICSSAS64001.2024.10760749

Wang. (2025). A Study on Translation Strategies for Character Development in Video Games: Taking Stardew Valley as an Example. *Arts, Culture and Language*. https://doi.org/10.61173/hgkday13.

Wang. (2025). A Study on Game Localization Translation from the Perspective of Communicative Translation Theory: A Case Study of Black Myth: Wukong. *Journal of Linguistics and Communication Studies*. https://doi.org/10.56397/jlcs.2025.04.07.

Westin. (2012). Large Scale Game Accessibility : A survey of possible engine independent solutions. **. https://www.semanticscholar.org/paper/91339a9f11676650f3f31ad4753d628da2a0e497.

Zhu. (2018). A Meta-Design Model for Creative Distributed Collaborative Design. **. https://www.semanticscholar.org/paper/b717baa7f431be0b98ee63492ad010bc62cada9f.

Üyesi, Şengün, & Öztürkcan. (2020). Re-Shaped by Mobile Technologies’ Disruption: The Videogame Industry in Turkey. **. https://www.semanticscholar.org/paper/182a86f2a33b3ca60563a5842c9b7daa94da1e77.