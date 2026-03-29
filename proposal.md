# Proposal

## What will (likely) be the title of your project?

PhenoCalc

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

This will be a script that allows the user to create punnet squares of any size  and it will produce a punnet square that shows the phenotype of each given combination. It will also give the odds of getting any given phenotype. 

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

So this script basically is to make calculating potential phenotypes as easy as possible, especially for Non-Mendelian genetics which can get pretty hairy. So, the first part of this will be to visualize punnet squares of any size (meaning they can input any given quantity of allele pairs such as Aa x aa | AaBb x aaBB | or even AaBBCcDDeeFf x AabbCCddEeff). Stuff like this can get pretty difficult once extending past one allele pair on paper, so a code would be really helpful. Extending this to non-Mendelian genetics means the script would ask the user if they want to include any type of epistatic relationships (Dominant Epistasis 1 or 2, reciprocal recessive epistasis, etc.) and then would include that consideration when producing the punnet square.

My complete list of interactions to include in the script: 
1) Mendelian
2) Incomplete Dominance
3) Co-Dominance
5) Multiple Alleles (i.e Ai > Ao > Ab > Ad)
6) Various forms of epistasis
7) Sex Linked inheritance

You can see a full list here if you're curious: https://en.wikipedia.org/wiki/Non-Mendelian_inheritance 

It would also use the mathematical rules we have in genetics in order to calculate the odds of getting any given phenotype given the users' inputs that visualized the punnet square: 1) Number of alleles. 2) Allele combinations 3) Mendelian or most forms of non-Mendelian genetics. 

This will also extend to sex chromosomes (X and Y) and the blood types (A+/-, B+/-, i). The code will account for the unique nature of these circumstances, so if the user enters them into the script, a different pathway will take over to accomodate the unique interactions they have (like sex-linked traits, and the recessive type O blood).

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

I think a good outcome, if all else fails will be to at least get the punnet square done and able to account for all of Mendlian genetics (pretty easy, there's only one set of rules) and the majority of Non-Mendlian genetics (more difficult because it has way more edge cases like recessive lethality). That being said, I think it would be pretty reasonable to do all of this since I understand the logic of genetics fairly well, since I have been studying this for 3 years now. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

I think a better outcome would be to have the punnet square done in it's entirety for all autosomal genetics, alongside the odds calculator. 

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

I think finishing all of it would be the ideal outcome. I want to see the script produce a punnet square for the autosomal and sex genes, as well as calculate the odds ratios for all phenotypic outcomes. 

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

The first thing will be figuring out how the phenotypes will be displayed in the punnet square, but I also want to find a way to make the matrix easy to look at, so I will most likely use a python library to make it more appealing. I will also need to refer to my genetics textbook to make sure I know how to write out the code for calculating each phenotype, as well as the non-Mendelian
and sex chomosomes interactions. My first step will be to go to my code file, and, in comments, write out the general workflow of the project. How I want the user to enter data, each method, what they will output, that way I know the general structure of the code, and from there can tackle them one at a time. 

I could foresee using Monte Carlo as a way to calculate the odds of each given phenotype, although I haven;t thought very hard about it and I'm not sure if that is the best way to proceed. It'll be an insane amount of 'for loops,' I can already tell; this entire project is just a gigantic "if, elif, else" statement inside and outside a lot of "for loops" in order to accomodate as many different forms of user entries as possible. 

I'm familiar with the Tabulate library as well, so I am considering using that to mkae my matrix visible. 
