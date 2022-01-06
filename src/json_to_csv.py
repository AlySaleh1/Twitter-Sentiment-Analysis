# Aly Saleh December 7th
# this script converts the outputted tweets from collect_tweets (which are json objects) to csv files
# each line in the input file is a json object
import json


# this functions converts a file of multiple json objects into a csv file
def json_to_csv(keyword_array):
    for word in keyword_array:
        input_file = '../data/txt/' + word + '.txt'
        output_file = '../data/csv/' + word + '.csv'

        # create headers, and then convert every line (which is a json object) into valid csv format
        with open(output_file, 'w') as output:
            output.write('\"ID\",\"TEXT\",\"CREATED_AT\",\"RETWEET_COUNT\",\"FAVOURITE_COUNT\",\"CATEGORY\",\"SENTIMENT\"\n')

            with open(input_file, 'r') as input_file_reader:
                for line in input_file_reader:
                    json_tweet = json.loads(line)
                    output.write(f'\"{json_tweet["id"]}\",\"{json_tweet["full_text"].encode("utf-8")}\",\"{json_tweet["created_at"]}\",\"{json_tweet["retweet_count"]}\",\"{json_tweet["favorite_count"]}\"\n')


def main():
    keywords = ['covid', 'vax', 'vaccination','moderna', 'astrazeneca', 'pfizer', 'vaccine']
    json_to_csv(keywords)


if __name__ == '__main__':
    main()
