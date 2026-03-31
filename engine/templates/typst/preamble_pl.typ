// OpenDraft — układ pod polskie uczelnie. Wymaga Typst ≥ 0.11 (par.first-line-indent, counter(page)).
#set page(
  margin: (left: 3.5cm, right: 2.5cm, top: 2.5cm, bottom: 2.5cm),
  numbering: "1",
  footer: context [
    #if counter(page).get().first() > 1 [
      #align(right)[#counter(page).display("1")]
    ]
  ],
)
#set text(font: ("Times New Roman", "Liberation Serif"), size: 12pt, lang: "pl")
#set par(justify: true, leading: 1.5em, first-line-indent: 1.25cm)
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
