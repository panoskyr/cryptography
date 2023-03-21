# The big idea
first we find the length of the key using the index of coincidence

We see that the key is 7 characters long so we now have to break a ceasar cipher for each of the 7 key characters

We use the cosine to get a sence of how similar each monoalphabetic substitution is for each of the 7 slides of the text.

So we examine each letter (26) for each slice (7)

The final dictionary has an ordered letter-cosine dictionary
By trying the first one for each slice we get AVOCADO that is the key

One could try more combination by combining the top4 of each candidate letter if the first ones did not work while also applying common sense (even if the cosine is close to 1 a substitution with many Z's or J's does not make sense)