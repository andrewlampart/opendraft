// OpenDraft — APA-style / US letter. Wymaga Typst ≥ 0.11 (par.first-line-indent, counter(page)).
#set page(
  margin: (x: 1in, y: 1in),
  numbering: "1",
  footer: context [
    #if counter(page).get().first() > 1 [
      #align(right)[#counter(page).display("1")]
    ]
  ],
)
#set text(font: ("Times New Roman", "Liberation Serif"), size: 12pt, lang: "en")
#set par(justify: true, leading: 2.0em, first-line-indent: 0.5in)
#show heading: it => {
  set par(first-line-indent: 0pt)
  it
}
#show heading.where(level: 1): it => {
  set align(center)
  set text(weight: "bold", size: 14pt)
  block(width: 100%, it)
}
#show table: it => block(width: 100%, breakable: true)[#it]
