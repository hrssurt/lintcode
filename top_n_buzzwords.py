import re
import heapq

numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]

def process_quote(quote):
	quote = quote.lower().split()
	quote = [re.sub('[^a-z]', '', w) for w in quote]
	return quote

def soln(numToys, topToys, toys, numQuotes, quotes):
	if not toys or topToys <= 0 or not quotes:
		return []

	toys = [t.lower() for t in toys]
	quotes = [process_quote(q) for q in quotes]
	d = {w: (0,0) for w in toys}
	for quote_lst in quotes:
		updated = set()
		for w in quote_lst:
			if w not in d:			# only care about relavent words(toys)
				continue	
			cur_occu_count, cur_quote_count = d[w]
			if w not in updated:
				cur_quote_count += 1
				updated.add(w)

			cur_occu_count += 1
			d[w] = (cur_occu_count, cur_quote_count)

	# some toys are not mentioned, we should not display them in the final result


	words = sorted([(-d[t][0], -d[t][1], t) for t in toys if d[t][0] != 0])
	return [w[2] for w in words][:topToys]






def online_soln_1(numToys, topToys, toys, numQuotes, quotes):
	import re
	N = topToys

	# create a dictionary --> toy:[count, quote_count]
	toys_freq = {toy:[0,0] for toy in toys}
	for quote in quotes:
	    # for each quote, initiate toy occurence to False
	    quote_toy = {toy:False for toy in toys}
	    # convert quote to lower case,split 
	    for word in quote.lower().split():
	        # remove anything other than lower cased letters in each word
	        word = re.sub('[^a-z]','',word)
	        # increment count of toy if it exists in toys dictionary
	        if word in toys_freq:
	            toys_freq[word][0] += 1
	            # if toy found in a quote, set to True and increment quote_count--> we do it only once for a toy in a quote
	            if not quote_toy[word]:
	                quote_toy[word] = True
	                toys_freq[word][1] += 1                
	# print toy, count, quote_count
	
	# sort by count descending, quote_count descending, alphabetically
	result = [w[0] for w in sorted(toys_freq.items(), key=lambda x: (-x[1][0],-x[1][1],x[0]))[:N]  if w[1][0] > 0]
	return result


def online_soln_2(numToys, topToys, toys, numQuotes, quotes):

    # Base case: if toys list is empty or quotes list is empty, the output list should also be []
    if not toys or not quotes:
        return []

    # Base case: if topToys are 0, that means we don't have to return any buzzwords
    if topToys == 0:
        return []

    # Dict to store toy buzzword as key and value as tuple in form of (total_freq, total_quotes)
    # So we will have dict like: {'elmo': (4, 3), 'elsa': (4, 2)}
    # Here, 'elmo': (4, 3) means word 'elmo' occurs total 4 times throughout all the quotes and it comes in 3 different quotes.
    #
    # We will first create entry for all toys with (total_freq, total_quotes) = (0, 0)
    toy_freq_quote = dict()
    for t in toys:
        toy_freq_quote[t] = (0, 0)

    # Iterate through all the quotes
    for q in quotes:
        # We need this updated_quote_count dict so that we don't increment the quote count for a buzzword more than once,
        # in case if it occurs multiple times in a single quote
        updated_quote_count = {toy: False for toy in toys}

        # Convert all the words to lowercase and split them.
        # Go through all the words of a quote and:
        #   - Remove all the extra characters from the words except "a-z". Basically we replace them with '' using regex.
        for w in q.lower().split():
            # We don't need to include A-Z in the regex, because we have already turned everything to lowercase before splitting.
            w = re.sub('[^a-z]', '', w)

            # Check if the current word is a toy/buzzword
            if toy_freq_quote.get(w):
                # Get current frequency and quote counts
                curr_freq, curr_quote = toy_freq_quote[w][0], toy_freq_quote[w][1]
                # If the current quote count is not already incremented for word w, do it and mark it in updated_quote_count
                if not updated_quote_count[w]:
                    curr_quote += 1
                    updated_quote_count[w] = True

                # Update freq and quote_count values
                toy_freq_quote[w] = (curr_freq+1, curr_quote)

    # Initially toy_freq_quote was created for all the given toys.
    # It is possible that some of those just don't appear in quotes.
    # Remove such toys from the toy_freq_quote whose frequency is 0
    for t in toys:
        if toy_freq_quote[t][0] == 0:
            del toy_freq_quote[t]

    # Now, we have the dict ready with all the buzzwords from toys list that come in quotes,
    # along with their total frequency and total quote count.
    #
    # First thing to check is if topToys (i.e. number of top toys/buzzwords to return) is > total numToys (i.e. total buzzwords)
    #   - If it is, then as per the given requirement, we just need to return the list of present buzzwords in quotes.
    #
    # If we return here, then all the computation stops and we are done.
    if topToys > numToys:
        return [toy for toy in toy_freq_quote]

    # Declare a list which we can use as heap.
    buzzword_heap = []

    # Go through all buzzwords from toy_freq_quote dict and take their (total_freq, total_quote_count).
    # Add it to the buzzword_heap as (-1*total_freq, -1*total_quote_count, buzzword)
    #
    # - Since we want to order by maximum total_freq and after that maximum total_quote_count, we will multiply them with -1 when
    #   pushing into the heap.
    # - We do that because in Python heapq.heapify(list), the heap created is min-heap.
    # - If we don't multiply those numbers by -1, then we will output with minimum total_freq and total_quotes.
    # - Also, we keep the ordering like (total_freq, total_quote_count, buzzword)
    #   because we first have to get the buzzword with max frequency, after that with max quote_count, and in the end
    #   in alphabetical order of buzzwords themselves.
    for toy in toy_freq_quote:
        total_freq, total_quote_count = toy_freq_quote[toy][0], toy_freq_quote[toy][1]
        buzzword_heap.append((-1*total_freq, -1*total_quote_count, toy))

    heapq.heapify(buzzword_heap)

    # Final result list
    top_buzzwords = []

    # Now we just do heappop equal to the total number of top buzzwords we have to return.
    # For every heappop, we will get back the tuple we have pushed:
    #   (total_freq, total_quote_count, buzzword)
    #
    # Since, in final output, all we need is buzzword, we just take the last element of the tuple, and append it to final list.
    for i in range(topToys):
        toy = heapq.heappop(buzzword_heap)[2]
        top_buzzwords.append(toy)

        # Check if there are any buzzwords left in the buzzword_heap or not.
        # There can be a case where we are asked to return top 5 buzzwords, but among all the quotes, only 3 buzzwords are present
        # In such case, we will return whatever buzzwords are present as per the sorting requirements given
        # This should be conveyed and discussed with interviewer
        if not buzzword_heap:
            break

    return top_buzzwords


if __name__ == '__main__':
	# some new test data:
	toys = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
	numToys = len(toys)
	topToys = 
	quotes = ["newshop is afshion providing good services in the city; everyone should use newshop", "best services by newshop", "fashionbeats has great services in the city", "i am proud to have fashionbeats", "mymarket has awesome services", "Thanks Newshop for the quick delivery afshion"]
	numQuotes = len(quotes)

	print(soln(numToys, topToys, toys, numQuotes, quotes))
	print(online_soln_1(numToys, topToys, toys, numQuotes, quotes))
	print(online_soln_2(numToys, topToys, toys, numQuotes, quotes))
