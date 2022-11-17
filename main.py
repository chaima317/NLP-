from extract import Extract
import matplotlib.pyplot as plt
ex= Extract()
ex.wordcloud.generate(ex.text)
fig, ax = plt.subplots(1,1, figsize = (9,6))
# add interpolation = bilinear to smooth things out
plt.imshow(ex.wordcloud, interpolation='bilinear')
# and remove the axis
plt.axis("off")
plt.show()
