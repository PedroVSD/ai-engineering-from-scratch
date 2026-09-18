const LESSONS = [
  { n: "01", slug: "01-estatistica-descritiva", title: "Estatística Descritiva do Zero", desc: "Média, mediana, IQR, z-score e histograma sem pandas.", fase: "Fase 04 · Estatística", tag: "piloto" },
  { n: "02", slug: "02-limpeza-e-eda", title: "Limpeza e EDA do Zero", desc: "Missing, duplicatas, Pearson do zero. Depois pandas.", fase: "Fase 06 · Wrangling", tag: "piloto" },
  { n: "03", slug: "03-regressao-do-zero", title: "Regressão Linear do Zero", desc: "Gradiente descendente manual, equação normal, R².", fase: "Fase 09 · Regressão", tag: "piloto" },
  { n: "04", slug: "04-classificacao-e-avaliacao", title: "Classificação e Avaliação", desc: "Logística + matriz de confusão + ROC/AUC.", fase: "Fase 10 · Classificação", tag: "piloto" },
  { n: "05", slug: "05-intro-deep-learning-perceptron", title: "Perceptron e Deep Learning do Zero", desc: "Perceptron falha no XOR. MLP + backprop resolve.", fase: "Fase 16 · DL Core", tag: "piloto" },
  { n: "06", slug: "06-probabilidade-fundamentos", title: "Probabilidade do Zero", desc: "Condicional, independência, lei total e Bayes (teste médico).", fase: "Fase 03 · Probabilidade", tag: "novo" },
  { n: "07", slug: "07-distribuicoes-tcl", title: "Distribuições e TCL", desc: "Bernoulli→Normal + simulação do Teorema Central do Limite.", fase: "Fase 03 · Probabilidade", tag: "novo" },
  { n: "08", slug: "08-clean-code-testes-ds", title: "Clean Code e Testes para DS", desc: "Pipeline modular, schema, pirâmide de testes. Notebook vs produção.", fase: "Fase 00 · Engenharia", tag: "novo" },
  { n: "09", slug: "09-reprodutibilidade-tracking", title: "Reprodutibilidade e Tracking", desc: "Seeds, hash de dataset, tracker JSONL (MLflow sem servidor).", fase: "Fase 00 · Engenharia", tag: "novo" },
];
const PHASES = [
  ["00", "Setup, Reprodutibilidade & Software Engineering", "18 aulas · Clean Code, testes, DVC, MLflow"],
  ["01", "Python, NumPy, Pandas, SciPy", "22 aulas · broadcasting, groupby, pivot"],
  ["02", "Matemática — Álgebra, Cálculo, Otimização", "24 aulas · SVD, Hessiana, Adam"],
  ["03", "Probabilidade", "18 aulas · 14 distribuições, TCL ✅ 2 aulas prontas"],
  ["04", "Estatística", "20 aulas · IC, testes, ANOVA ✅ 1 pronta"],
  ["05", "Aquisição, SQL & Modelagem", "22 aulas · window, lakehouse"],
  ["06", "Data Quality & Wrangling", "20 aulas · Box-Cox, LOF ✅ 1 pronta"],
  ["07", "EDA, Visualização & Storytelling", "18 aulas"],
  ["08", "Fundamentos ML & Baselines", "16 aulas · leakage"],
  ["09", "Regressão & Regularização", "16 aulas ✅ 1 pronta"],
  ["10", "Classificação", "18 aulas · XGBoost ✅ 1 pronta"],
  ["11", "Avaliação, Validação & Tuning", "20 aulas · Nested CV, BayesOpt"],
  ["12", "Feature Engineering", "16 aulas · Feature Store"],
  ["13", "Não-Supervisionado & Anomalias", "18 aulas"],
  ["14", "Séries Temporais", "16 aulas · ARIMA, Prophet"],
  ["15", "Recomendação & NLP", "20 aulas · NDCG, BERT"],
  ["16", "Deep Learning Core", "18 aulas ✅ 1 pronta"],
  ["17", "Arquiteturas DL", "18 aulas · CNN/RNN/Transformer"],
  ["18", "Experimentação, Causalidade, XAI", "16 aulas · SHAP, DiD"],
  ["19", "MLOps, Produção & Capstones", "28 aulas · K8s, drift, RAG"],
];
function render(filter = "") {
  const q = filter.toLowerCase();
  const grid = document.getElementById("lessons");
  grid.innerHTML = "";
  LESSONS.filter(l => (l.title + l.desc + l.fase).toLowerCase().includes(q)).forEach(l => {
    const d = document.createElement("div");
    d.className = "card";
    d.innerHTML = `<h3>${l.n} — ${l.title} <span class="badge ${l.tag}">${l.tag}</span></h3><p class="muted">${l.fase}</p><p>${l.desc}</p><pre>python phases/20-data-science-foundations/${l.slug}/code/main.py</pre><a href="../phases/20-data-science-foundations/${l.slug}/docs/en.md">docs</a> · <a href="../phases/20-data-science-foundations/${l.slug}/quiz.json">quiz</a>`;
    grid.appendChild(d);
  });
  const pg = document.getElementById("phases");
  pg.innerHTML = "";
  PHASES.forEach(([id, name, info]) => {
    const done = ["00", "03", "04", "06", "09", "10", "16"].includes(id);
    const d = document.createElement("div");
    d.className = "phase" + (done ? " done" : "");
    d.innerHTML = `<b>${id} · ${name}</b><br><span class="muted">${info}</span>`;
    pg.appendChild(d);
  });
  document.getElementById("count").textContent = `${LESSONS.length} aulas implementadas · ~642 planejadas`;
}
document.addEventListener("DOMContentLoaded", () => {
  render();
  document.getElementById("search").addEventListener("input", e => render(e.target.value));
});
