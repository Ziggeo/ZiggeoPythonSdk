This readme will show you how to run demos and how they are organized

# How to call demos through console

If you want to use the code from `videos_count.py` you would want to open it and see what parameters it requires.

In its case this is important to us
```
app_token = sys.argv[1]
private_key = sys.argv[2]
```

It means that we need to pass `app_token` and `private_key` to our script.

## We would do it like so:

```python videos_count.py APP_TOKEN PRIVATE_KEY```

So every file will have its own parameters, however they will always be called out like so:

```python filename.py parameter1_value parameter2_value```

# Organization

The demos are organized by the class and function name. So for example if you want to see how to get the count of the videos you would find it in the name that matches the same:
 1. videos()
 2. count()

...making the filename "videos_count.py"

The scripts that are created to help with different things like benchmarks (_benchmark.py) and alike, are prefixed with an underscore and then match the similar structure as above to help you separate it all (however they can have any filename that describes action or multiple actions).
