# ASGCheck

Check AWS autoscaling groups in one or many regions for bound load balancers that no longer exist, optionally report results to Slack. This project is extremely low-tech, use at your own risk!

You'll need an IAM policy that allows:

- `describe_load_balancers`
- `get_asg_bound_elbs`


### Usage

```
$ export AWS_PROFILE="foo"
$ export ASGCHECK_SLACK_TOKEN="foobar123"
$ python3 asgcheck.py -r us-west-2,ap-northeast-1 -s some-slack-channel 
```

### LICENSE

See `LICENSE` file.
