# training schedule for maskflownet_ft schedule
train_cfg = dict(by_epoch=False, max_iters=1000000, val_interval=50000)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

# optimizer
optimizer_config = dict(
    type='OptimWrapper',
    optimizer=dict(
        type='Adam', lr=5e-5, weight_decay=0.0004, betas=(0.9, 0.999)))

# learning policy
param_scheduler = dict(
    type='MultiStageLR',
    by_epoch=False,
    gammas=[0.5, 0.5, 0.5, 0.5, 0.5],
    milestone_params=[5e-5, 3e-5, 2e-5, 1e-5, 5e-6],
    milestone_iters=[0, 200000, 400000, 600000, 800000],
    steps=[[100000, 150000], [300000, 350000], [500000, 550000],
           [700000, 750000], [850000, 875000, 900000, 950000, 975000]])
