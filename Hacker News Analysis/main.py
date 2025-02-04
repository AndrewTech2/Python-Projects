import pandas

df = pandas.read_csv('hacker_news.csv')
ask_hn = []
show_hn = []
for ind, post in df.iterrows():
    if post['title'].lower().startswith("ask hn"):
        ask_hn.append(post)
    elif post['title'].lower().startswith("show hn"):
        show_hn.append(post.to_dict())

ask_hn = pandas.DataFrame(ask_hn)
show_hn = pandas.DataFrame(show_hn)
avg_ask = ask_hn['num_comments'].mean()
avg_show = show_hn['num_comments'].mean()
if avg_ask > avg_show:
    print("Ask HN posts get more comments than Show HN posts.")
else:
    print("Show HN posts get more comments than Ask HN posts.")
print()
hours = []
for ind, post in ask_hn.iterrows():
    hour = int(post['created_at'].split()[1].split(":")[0])
    hours.append(hour)
ask_hn['hour'] = hours
mean_by_hour = ask_hn.groupby("hour")['num_comments'].mean().to_dict()
sorted_hours = sorted(mean_by_hour, key=lambda x: mean_by_hour[x], reverse=True)
print("Most popular first 5 hours to comment on Ask HN posts:")
for hour in sorted_hours[:6]:
    print(f"{0 if len(str(hour)) == 1 else ''}{hour}:00: {round(mean_by_hour[hour], 2)} average comments")