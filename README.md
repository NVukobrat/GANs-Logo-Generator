# Summary
Creating logo images using Generative Adversarial Networks (GANs).

This project uses GANs models to produce new logo images. It works by trying to mimic real-world images collected from the Wikipedia pages. More details about GANs are provided in the overview.

Also, bellow is specified OS and Hardware elements used during this project R&D, explanation of the used dataset, results in section and analysis section. In the result section, most of the documentation consists of cases in which models were trained. Those cases consist of conclusions, generator samples on arbitrarily chosen epochs, and generator accuracy for that case. These cases are intended to give more intuition on how GANs tries to solve the given problem. In the analysis section, more details graphics are provided in order to get better intuition about what happening during the training process.

## GANs overview
Generative Adversarial Networks (GANs) belongs to the generative models. That means they are able to generate artificial content base on the arbitrary input.

Generally, GANs most of the time refers to the training method, rather on the generative model. Reason for this is that GANs don't train a single network, but instead two networks simultaneously.

The first network is usually called Generator, while the second Discriminator. Purpose of the Generator model is to images that look real. During training, the Generator progressively becomes better at creating images that look real. Purpose of the Discriminator model is to learn to tell real images apart from fakes. During training, the Discriminator progressively becomes better at telling fake images from real ones. The process reaches equilibrium when the Discriminator can no longer distinguish real images from fakes.

## Environment
- **OS:** Ubuntu 19.04
- **Processor:** Intel Core i7-4770 CPU @ 3.40GHz × 8
- **Graphics:** GeForce GTX 1080 Ti/PCIe/SSE2
- **Memory:** Kingston HyperX Fury Red 16 GB (2 x 8 GB)
- **Language:** Python 3.5.2 with TensorFlow 2.0.0b1 (Dockerized version)

## Dataset
The dataset used for generating logo images comes from [Large Logo Dataset (LLD)](https://data.vision.ee.ethz.ch/sagea/lld/). Concretely, from a [sample of 5.000 images](https://data.vision.ee.ethz.ch/sagea/lld/data/LLD-icon_sample.zip) in the PNG format. Shape of images is 32x32x3, where they represent Width, Height and Channels respectively. Images are collected from the Wikipedia descriptions by looking for favicon.ico sample.

## Notes
- The last **Case 3** is still in the training process. Presented results are only current results. This case will last at least 500.000 epoch. If it start to generate good results, this could be prolonged to even more epochs.

# Results

## Case 1
This case uses the whole dataset that contains **5.000** logo samples. It iterates over **230.000** epochs with **256** batch size. The total execution time of this case is **6d 10h 39m 59s**.

As you can see, the generator model tries to generate real-looking logo images by mimic the value and distribution of the pixels of each image batch. Generator model converges well until 167.000 epoch. Then, it overfits to the one combination of samples and generates a very similar image each time. This maybe could be solved by longer training or/and bigger dataset, but this requires additional hardware resource in order to speed up the training process. From the discriminator perspective, it does very well in determining which images are real, and which are fake with almost 100% accuracy. 

### Generator Results
<table>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00100_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00200_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00300_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00400_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00500_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00600_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00700_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00800_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_00900_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01100_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01200_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01300_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01400_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01500_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01600_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01700_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01800_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_01900_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_02000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_03000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_04000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_05000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_06000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_07000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_08000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_09000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_10000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_11000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_12000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_13000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_14000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_15000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_16000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_17000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_18000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_19000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_20000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_21000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_22000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_23000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_24000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_25000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_26000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_27000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_28000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_29000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_30000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_31000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_32000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_33000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_34000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_35000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_36000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_37000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_38000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_39000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_40000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_41000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_42000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_43000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_44000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_45000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_46000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_47000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_48000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_49000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_50000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_51000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_52000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_53000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_54000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_55000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_56000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_57000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_58000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_59000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_60000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_61000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_62000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_63000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_64000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_65000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_66000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_67000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_68000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_69000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_70000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_71000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_72000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_73000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_74000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_75000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_76000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_77000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_78000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_79000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_80000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_81000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_82000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_83000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_84000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_85000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_86000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_87000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_88000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_89000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_90000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_91000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_92000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_93000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_94000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_95000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_96000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_97000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_98000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_99000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_100000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_101000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_102000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_103000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_104000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_105000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_106000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_107000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_108000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_109000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_110000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_111000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_112000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_113000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_114000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_115000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_116000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_117000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_118000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_119000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_120000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_121000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_122000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_123000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_124000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_125000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_126000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_127000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_128000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_129000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_130000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_131000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_132000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_133000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_134000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_135000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_136000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_137000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_138000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_139000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_140000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_141000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_142000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_143000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_144000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_145000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_146000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_147000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_148000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_149000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_150000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_151000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_152000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_153000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_154000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_155000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_156000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_157000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_158000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_159000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_160000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_161000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_162000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_163000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_164000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_165000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_166000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_167000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_168000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_169000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_170000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_171000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_172000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_173000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_174000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_175000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_176000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_177000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_178000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_179000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_180000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_181000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_182000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_183000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_184000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_185000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_186000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_187000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_188000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_189000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_190000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_191000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_192000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_193000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_194000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_195000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_196000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_197000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_198000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_199000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_200000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_201000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_202000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_203000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_204000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_205000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_206000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_207000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_208000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_209000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_210000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_211000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_212000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_213000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_214000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_215000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_216000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_217000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_218000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_219000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_220000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_221000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_222000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_223000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_224000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_225000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_226000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_227000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_228000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_229000_00000.png" alt=""></td>
		<td><img src="assets/images/case_1/generator_results/image_at_epoch_230000_00000.png" alt=""></td>
	</tr>
</table>

### Discriminator Accuracy
<table>
    <tr>
        <td>Discriminator on real images</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/discriminator_accuracy/Accuracy_Real Discriminator.png" alt=""></td>
    </tr>
    <tr>
        <td>Discriminator on fake images</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/discriminator_accuracy/Accuracy_Fake Discriminator.png" alt=""></td>
    </tr>
    <tr>
        <td>Discriminator combined mean loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/discriminator_accuracy/Accuracy_Combined Discriminator.png" alt=""></td>
    </tr>
</table>


## Case 2
This case uses a small part of the dataset that contains **100** logo samples. It iterates over **760.000** epochs with **100** batch size. The total execution time of this case is **1d 15h 3m 19s**.

Because of the very tiny dataset size, generator, in this case, overfits really fast. At 32.000 epoch, it already overfits and generates logo samples from the dataset. Till the end of the training, it keeps generating images too much similar to the training ones. Discriminator does very well in this case too, with almost 100% accuracy.

In the generator results, only images till 201.000 epoch are shown. Rest of the samples are similar till 760.000 epochs.

### Generator Results
<table>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00100_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00200_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00300_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00400_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00500_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00600_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00700_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00800_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_00900_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01100_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01200_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01300_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01400_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01500_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01600_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01700_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01800_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_01900_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_02000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_03000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_04000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_05000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_06000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_07000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_08000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_09000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_10000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_11000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_12000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_13000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_14000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_15000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_16000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_17000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_18000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_19000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_20000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_21000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_22000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_23000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_24000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_25000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_26000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_27000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_28000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_29000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_30000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_31000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_32000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_33000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_34000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_35000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_36000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_37000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_38000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_39000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_40000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_41000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_42000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_43000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_44000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_45000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_46000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_47000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_48000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_49000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_50000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_51000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_52000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_53000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_54000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_55000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_56000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_57000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_58000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_59000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_60000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_61000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_62000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_63000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_64000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_65000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_66000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_67000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_68000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_69000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_70000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_71000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_72000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_73000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_74000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_75000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_76000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_77000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_78000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_79000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_80000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_81000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_82000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_83000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_84000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_85000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_86000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_87000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_88000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_89000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_90000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_91000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_92000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_93000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_94000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_95000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_96000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_97000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_98000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_99000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_100000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_101000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_102000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_103000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_104000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_105000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_106000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_107000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_108000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_109000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_110000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_111000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_112000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_113000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_114000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_115000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_116000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_117000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_118000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_119000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_120000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_121000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_122000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_123000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_124000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_125000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_126000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_127000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_128000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_129000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_130000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_131000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_132000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_133000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_134000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_135000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_136000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_137000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_138000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_139000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_140000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_141000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_142000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_143000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_144000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_145000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_146000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_147000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_148000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_149000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_150000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_151000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_152000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_153000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_154000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_155000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_156000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_157000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_158000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_159000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_160000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_161000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_162000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_163000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_164000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_165000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_166000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_167000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_168000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_169000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_170000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_171000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_172000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_173000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_174000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_175000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_176000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_177000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_178000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_179000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_180000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_181000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_182000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_183000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_184000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_185000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_186000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_187000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_188000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_189000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_190000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_191000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_192000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_193000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_194000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_195000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_196000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_197000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_198000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_199000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_200000_00000.png" alt=""></td>
		<td><img src="assets/images/case_2/generator_results/image_at_epoch_201000_00000.png" alt=""></td>
	</tr>
</table>

### Discriminator Accuracy
<table>
    <tr>
        <td>Discriminator on real images</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/discriminator_accuracy/Accuracy_Real Discriminator.png" alt=""></td>
    </tr>
    <tr>
        <td>Discriminator on fake images</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/discriminator_accuracy/Accuracy_Fake Discriminator.png" alt=""></td>
    </tr>
    <tr>
        <td>Discriminator combined mean loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/discriminator_accuracy/Accuracy_Combined Discriminator.png" alt=""></td>
    </tr>
</table>

## Case 3
This case uses almost whole dataset that contains **4096/5000** logo samples. It iterates over **400.000** epochs with **1024** batch size. The total execution time of this case is **8d 21h 55m 18s**. 

### Generator Results
<table>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00100_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00200_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00300_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00400_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00500_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00600_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00700_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00800_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_00900_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01100_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01200_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01300_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01400_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01500_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01600_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01700_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01800_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_01900_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_02000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_03000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_04000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_05000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_06000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_07000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_08000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_09000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_10000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_11000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_12000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_13000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_14000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_15000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_16000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_17000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_18000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_19000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_20000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_21000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_22000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_23000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_24000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_25000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_26000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_27000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_28000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_29000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_30000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_31000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_32000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_33000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_34000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_35000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_36000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_37000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_38000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_39000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_40000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_41000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_42000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_43000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_44000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_45000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_46000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_47000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_48000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_49000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_50000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_51000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_52000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_53000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_54000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_55000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_56000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_57000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_58000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_59000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_60000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_61000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_62000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_63000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_64000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_65000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_66000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_67000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_68000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_69000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_70000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_71000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_72000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_73000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_74000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_75000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_76000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_77000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_78000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_79000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_80000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_81000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_82000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_83000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_84000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_85000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_86000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_87000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_88000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_89000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_90000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_91000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_92000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_93000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_94000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_95000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_96000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_97000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_98000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_99000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_100000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_101000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_102000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_103000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_104000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_105000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_106000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_107000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_108000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_109000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_110000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_111000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_112000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_113000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_114000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_115000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_116000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_117000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_118000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_119000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_120000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_121000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_122000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_123000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_124000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_125000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_126000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_127000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_128000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_129000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_130000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_131000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_132000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_133000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_134000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_135000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_136000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_137000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_138000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_139000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_140000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_141000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_142000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_143000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_144000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_145000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_146000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_147000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_148000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_149000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_150000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_151000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_152000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_153000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_154000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_155000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_156000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_157000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_158000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_159000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_160000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_161000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_162000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_163000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_164000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_165000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_166000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_167000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_168000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_169000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_170000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_171000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_172000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_173000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_174000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_175000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_176000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_177000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_178000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_179000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_180000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_181000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_182000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_183000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_184000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_185000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_186000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_187000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_188000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_189000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_190000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_191000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_192000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_193000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_194000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_195000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_196000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_197000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_198000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_199000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_200000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_201000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_202000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_203000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_204000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_205000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_206000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_207000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_208000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_209000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_210000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_211000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_212000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_213000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_214000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_215000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_216000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_217000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_218000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_219000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_220000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_221000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_222000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_223000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_224000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_225000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_226000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_227000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_228000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_229000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_230000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_231000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_232000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_233000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_234000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_235000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_236000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_237000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_238000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_239000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_240000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_241000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_242000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_243000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_244000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_245000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_246000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_247000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_248000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_249000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_250000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_251000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_252000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_253000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_254000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_255000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_256000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_257000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_258000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_259000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_260000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_261000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_262000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_263000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_264000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_265000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_266000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_267000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_268000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_269000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_270000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_271000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_272000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_273000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_274000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_275000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_276000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_277000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_278000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_279000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_280000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_281000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_282000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_283000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_284000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_285000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_286000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_287000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_288000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_289000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_290000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_291000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_292000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_293000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_294000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_295000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_296000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_297000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_298000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_299000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_300000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_301000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_302000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_303000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_304000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_305000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_306000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_307000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_308000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_309000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_310000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_311000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_312000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_313000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_314000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_315000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_316000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_317000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_318000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_319000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_320000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_321000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_322000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_323000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_324000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_325000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_326000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_327000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_328000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_329000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_330000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_331000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_332000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_333000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_334000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_335000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_336000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_337000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_338000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_339000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_340000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_341000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_342000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_343000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_344000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_345000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_346000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_347000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_348000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_349000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_350000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_351000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_352000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_353000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_354000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_355000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_356000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_357000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_358000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_359000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_360000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_361000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_362000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_363000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_364000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_365000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_366000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_367000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_368000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_369000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_370000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_371000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_372000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_373000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_374000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_375000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_376000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_377000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_378000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_379000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_380000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_381000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_382000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_383000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_384000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_385000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_386000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_387000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_388000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_389000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_390000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_391000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_392000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_393000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_394000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_395000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_396000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_397000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_398000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_399000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_400000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_401000_00000.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_402000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_403000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_404000_00000.png" alt=""></td>
		<td><img src="assets/images/case_3/generator_results/image_at_epoch_405000_00000.png" alt=""></td>
	</tr>
</table>

### Discriminator Accuracy
<table>
    <tr>
        <td>Discriminator on real images</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/discriminator_accuracy/Accuracy_Real Discriminator.png" alt=""></td>
    </tr>
    <tr>
        <td>Discriminator on fake images</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/discriminator_accuracy/Accuracy_Fake Discriminator.png" alt=""></td>
    </tr>
    <tr>
        <td>Discriminator combined mean loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/discriminator_accuracy/Accuracy_Combined Discriminator.png" alt=""></td>
    </tr>
</table>

# Analysis

## Case 1

### Loss
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/loss/Loss_Generator.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/loss/Loss_Discriminator.png" alt=""></td>
    </tr>
</table>

### Histograms
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/histogram/histogram_1.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/histogram/histogram_2.png" alt=""></td>
    </tr>
</table>

### Distribution
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/distribution/distribution_1.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/distribution/distribution_2.png" alt=""></td>
    </tr>
</table>

### Training Speed
<table>
    <tr>
        <td>Sum epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/execution_time/Execution time_Sum epoch.png" alt=""></td>
    </tr>
    <tr>
    	<td>Average epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/execution_time/Execution time_Average epoch.png" alt=""></td>
    </tr>
    <tr>
    	<td>Train epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_1/execution_time/Execution time_Train epoch.png" alt=""></td>
    </tr>
</table>

## Case 2

### Loss
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/loss/Loss_Generator.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/loss/Loss_Discriminator.png" alt=""></td>
    </tr>
</table>

### Histograms
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/histogram/histogram_1.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/histogram/histogram_2.png" alt=""></td>
    </tr>
</table>

### Distribution
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/distribution/distribution_1.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/distribution/distribution_2.png" alt=""></td>
    </tr>
</table>

### Training Speed
<table>
    <tr>
        <td>Sum epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/execution_time/Execution time_Sum epoch.png" alt=""></td>
    </tr>
    <tr>
    	<td>Average epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/execution_time/Execution time_Average epoch.png" alt=""></td>
    </tr>
    <tr>
    	<td>Train epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_2/execution_time/Execution time_Train epoch.png" alt=""></td>
    </tr>
</table>

## Case 3

### Loss
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/loss/Loss_Generator.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/loss/Loss_Discriminator.png" alt=""></td>
    </tr>
</table>

### Histograms
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/histogram/histogram_1.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/histogram/histogram_2.png" alt=""></td>
    </tr>
</table>

### Distribution
<table>
    <tr>
        <td>Generator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/distribution/distribution_1.png" alt=""></td>
    </tr>
    <tr>
    	<td>Discriminator Loss</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/distribution/distribution_2.png" alt=""></td>
    </tr>
</table>

### Training Speed
<table>
    <tr>
        <td>Sum epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/execution_time/Execution time_Sum epoch.png" alt=""></td>
    </tr>
    <tr>
    	<td>Average epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/execution_time/Execution time_Average epoch.png" alt=""></td>
    </tr>
    <tr>
    	<td>Train epoch</td>
    </tr>
    <tr>
        <td><img src="assets/images/case_3/execution_time/Execution time_Train epoch.png" alt=""></td>
    </tr>
</table>