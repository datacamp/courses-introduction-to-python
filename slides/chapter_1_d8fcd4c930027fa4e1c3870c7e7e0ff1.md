---
title: Insert title here
key: d8fcd4c930027fa4e1c3870c7e7e0ff1
video_link:
  mp3: >-
    https://videos.datacamp.com/mp3/translations/course_735/pt-BR/db068946-3d72-4477-ab32-cdbf852fd0ee.mp3
---

## Olá, Python!

```yaml
type: TitleSlide
key: f743ca8c41
```

`@lower_third`
name: Hugo Bowne-Anderson
title: Data Scientist at DataCamp

`@script`
Oi, meu nome é Hugo, e serei o apresentador da Introdução ao Python para Ciência de Dados.

Sou cientista de dados e instrutor do DataCamp.


---

## Como você vai aprender

```yaml
type: FullSlide
key: 30ee08a725
disable_transition: true
```

`@part1`
![Interface do DataCamp](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/729574d2168960686381caefe79baf5978e27d0d/liveexercise.gif)

`@script`
Neste curso, você vai aprender Python para Ciência de Dados com aulas em vídeo, como esta, e exercícios interativos. Você tem sua própria sessão Python, onde pode fazer testes e tentar descobrir o código certo para resolver as instruções. Você vai aprender na prática, enquanto recebe feedback personalizado e imediato sobre o trabalho.


---

## Python

```yaml
type: FullSlide
key: 3f23b93572
```

`@part1`
![guido-hba.png](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/fb3e4b8dc114529dafffb37d33f2b2244210d40f/guido-hba.png = 38){{1}}

- Uso geral: desenvolver qualquer coisa{{2}}

- Código aberto! Grátis!{{3}}

- Pacotes Python, também para ciência de dados{{4}}

	- Muitas aplicações em diversas áreas{{5}}

`@script`
O Python foi criado por Guido Van Rossum. Aqui, você pode ver uma foto minha com o Guido. Um projeto que começou como um hobby logo virou uma linguagem de programação de uso geral: hoje em dia, dá para usar Python para criar praticamente qualquer tipo de software. Como isso aconteceu? Bem, primeiro, o Python tem código aberto. Seu uso é grátis. Segundo, é muito fácil criar pacotes em Python, que são códigos que podemos compartilhar com outras pessoas para resolver determinados problemas. Com o tempo, foram criados cada vez mais pacotes desenvolvidos especialmente para ciência de dados. Suponha que você queira fazer umas visualizações legais das vendas da sua empresa. Existe um pacote para isso. E que tal acessar um banco de dados para analisar medições de sensores? Também existe um pacote para isso.
As pessoas costumam chamar o Python de canivete suíço das linguagens de programação, porque dá para fazer quase tudo com ele.
Neste curso, vamos começar a desenvolver suas habilidades de programação em ciência de dados aos poucos, então fique por aqui para ver como essa linguagem pode ser poderosa.


---

## Shell IPython

```yaml
type: FullSlide
key: 43a91a7217
```

`@part1`
**Execução de comandos Python**

![ipython_shell.png](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png = 95)

`@script`
Agora que você está com toda a atenção voltada para o Python, vamos fazer alguns testes. Vou começar com o


---

## Shell IPython

```yaml
type: FullSlide
key: 9c51ee700d
disable_transition: true
```

`@part1`
**Execução de comandos Python**

![ipython_shell_highlighted.png](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/dd43cc0183b15b43a072eb0fbab4caa72dee9250/pyexercise_shell.jpg = 95)

`@script`
shell Python, um lugar onde você pode digitar código Python e ver os resultados na hora. Na interface de exercícios do DataCamp, esse shell está integrado aqui. Vamos começar com algo simples e usar o Python como calculadora.


---

## Shell IPython

```yaml
type: FullSlide
key: 524e4c20a7
disable_transition: true
```

`@part1`
&nbsp;

![Cálculos no shell IPython do DataCamp](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/cee32b788a62e4b9a1234ccde56ac9ebb49cfa72/shelladdition.gif = 95)

`@script`
Vou digitar quatro mais cinco e dar Enter. O Python entende o que você digitou e imprime o resultado da conta, nove. O shell Python que usamos aqui não é o original. Estamos utilizando o IPython, abreviação de Interactive Python, uma versão melhorada do Python normal que vai ser útil mais tarde.

O IPython foi criado por Fernando Pérez e faz parte do Jupyter, um ecossistema maior. Além de trabalhar com o Python de modo interativo, também podemos fazer com que o Python rode os chamados


---

## Script Python

```yaml
type: FullSlide
key: 78ef256bc0
```

`@part1`
- Arquivos de texto – `.py`{{1}}

- Lista de comandos Python{{2}}

- Parecido com digitar no shell IPython{{3}}

![Script Python no DataCamp](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/59f196e96536543a4fb8801228019fc4106f3791/pyexercise_script.jpg = 78){{3}}

`@script`
scripts Python. Esses scripts Python são simplesmente arquivos de texto com a extensão ponto py. É basicamente uma lista de comandos Python que são executados, como se estivéssemos digitando os comandos no shell, linha por linha.


---

## Script Python

```yaml
type: FullSlide
key: 717d124175
disable_transition: true
```

`@part1`
![GIF: digitando 4 + 5 no script e clicando em enviar resposta. Nenhuma saída é mostrada.](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/2f96e979012e15329cc158d1e0f496aac3539f45/scriptnoprint.gif = 95)

`@script`
Agora vamos colocar o comando anterior em um script, que pode ser encontrado aqui na interface do DataCamp. O próximo passo é rodar o script, clicando em “Enviar resposta”. Se você rodar esse script na interface do DataCamp, não vai aparecer nada no painel de saída. Isso porque você precisa usar print explicitamente nos scripts se quiser gerar uma saída durante a execução.


---

## Script Python

```yaml
type: FullSlide
key: c7a9d02fb6
disable_transition: true
code_zoom: 90
```

`@part1`
![python_script_print.gif](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/8b13d046bb54dcb11aa49f0da7363781129d1561/scriptwithprint.gif = 95)

- Use `print()` para gerar uma saída a partir do script

`@script`
Vamos colocar o cálculo anterior em uma chamada de print e rodar o script de novo. Dessa vez, foi gerada a mesma saída de antes. Ótimo! Colocar seus códigos em scripts Python em vez de digitar manualmente cada passo de forma interativa ajuda a manter a estrutura e evita ter que digitar tudo de novo se você quiser fazer uma mudança. Basta fazer a alteração no script e executar tudo de novo.


---

## Interface do DataCamp

```yaml
type: FullSlide
key: 693ba1cd14
```

`@part1`
![Captura de tela da interface do DataCamp](https://assets.datacamp.com/img/translations/pt-BR/production/repositories/288/datasets/a9e8440bb8fbd49e4a73e4c36ef1cd677c0dd55f/pyexercise.png)

`@script`
Agora que você já tem uma ideia das diferentes maneiras de trabalhar com o Python, sugiro que vá para os exercícios. Use o shell IPython para fazer testes e use o editor de scripts Python para programar a resposta em si. Se você clicar em Enviar resposta, o script vai ser executado para verificar se está certo.


---

## Vamos praticar!

```yaml
type: FinalSlide
key: 7445cd202e
```

`@script`
Comece a programar e divirta-se!
