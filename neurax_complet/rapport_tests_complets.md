# Rapport de Test Complet du Réseau Neuronal Gravitationnel Quantique (Neurax)

Date: 2025-05-13 03:33:07

## Résumé

- **Total des tests**: 15
- **Tests réussis**: 13
- **Tests échoués**: 1
- **Tests ignorés**: 1
- **Taux de réussite**: 86.67%
- **Temps d'exécution total**: 1.53 secondes

## Configuration Matérielle

- **Système**: posix
- **CPU Logiques**: 8
- **CPU Physiques**: 4
- **Mémoire Totale**: 62.81 GB
- **Mémoire Disponible**: 28.99 GB
- **Version Python**: 3.11.10
- **Version NumPy**: 2.2.5

## Résultats Détaillés par Composant

### ✅ Simulateur de Gravité Quantique

- **Tests**: 9
- **Réussis**: 9
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 0.0288 | initialization_ok: True, shape_ok: True, expected_shape: (4, 20, 20, 20), actual_shape: (4, 20, 20, 20), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 1.4199615103609387, 'max_change': 156.62193248397648, 'min_val': -103.35319502193644, 'max_val': 156.62193248397648, 'mean_val': -0.010140317498730124, 'std_val': 5.016652224474699}, 1.0: {'has_changes': True, 'avg_change': 2.9574918193109188, 'max_change': 252.44269972713303, 'min_val': -254.6422842413936, 'max_val': 208.9763582518046, 'mean_val': -0.005058512296286249, 'std_val': 11.696572929767699}, 2.0: {'has_changes': True, 'avg_change': 5.8904947856545675, 'max_change': 387.7539566162102, 'min_val': -393.2485705005165, 'max_val': 315.2466275159698, 'mean_val': 0.07359024870474226, 'std_val': 23.57695967210309}}, simulation_steps_results: {1: {'avg_step_time': 0.0028717517852783203, 'metrics': {'timestamp': '2025-05-13T03:33:07.954924', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0008627891540527344, 'metrics': {'timestamp': '2025-05-13T03:33:07.959290', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': -4.5652818616780104e-08, 'max_curvature': 0.00021681173092459927, 'min_curvature': -0.00017188297020822305, 'std_deviation': 2.1104651846695277e-05, 'total_energy': 0.09514990549970452, 'quantum_density': 7.358825190166953e+29}}, 10: {'avg_step_time': 0.0008030176162719726, 'metrics': {'timestamp': '2025-05-13T03:33:07.967349', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -4.796134236405598e-07, 'max_curvature': 0.00034057964170087536, 'min_curvature': -0.0003255082717497151, 'std_deviation': 4.275700151228536e-05, 'total_energy': 0.24282236022196674, 'quantum_density': 1.8779706524698036e+30}}} |
| Test 2 | ✅ Réussi | 0.0393 | initialization_ok: True, shape_ok: True, expected_shape: (8, 20, 20, 20), actual_shape: (8, 20, 20, 20), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.734806364490061, 'max_change': 139.23050068267298, 'min_val': -104.58417472849322, 'max_val': 139.23050068267298, 'mean_val': 0.003103579918254298, 'std_val': 3.648823862743437}, 1.0: {'has_changes': True, 'avg_change': 1.4539425561067891, 'max_change': 236.3723166132523, 'min_val': -236.53556245734822, 'max_val': 231.96958164373427, 'mean_val': -0.009362401391933445, 'std_val': 8.341235273264443}, 2.0: {'has_changes': True, 'avg_change': 3.000044625730686, 'max_change': 559.1244999453401, 'min_val': -381.5264401135712, 'max_val': 571.3625968782851, 'mean_val': -0.012485025479375857, 'std_val': 17.42252093754906}}, simulation_steps_results: {1: {'avg_step_time': 0.001863718032836914, 'metrics': {'timestamp': '2025-05-13T03:33:07.985403', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0008594512939453125, 'metrics': {'timestamp': '2025-05-13T03:33:07.989766', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.0016849279403686524, 'metrics': {'timestamp': '2025-05-13T03:33:08.006635', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 7.283334726314777e-07, 'max_curvature': 0.0002814374763785621, 'min_curvature': -0.00020926526218203778, 'std_deviation': 2.9768002932587e-05, 'total_energy': 0.1532287929106802, 'quantum_density': 1.1850604529854108e+30}}} |
| Test 3 | ✅ Réussi | 0.0237 | initialization_ok: True, shape_ok: True, expected_shape: (16, 20, 20, 20), actual_shape: (16, 20, 20, 20), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.376756350567496, 'max_change': 136.95108458762303, 'min_val': -136.95108458762303, 'max_val': 109.28592315751123, 'mean_val': -0.004927476289571459, 'std_val': 2.6898368700748487}, 1.0: {'has_changes': True, 'avg_change': 0.7417948479650862, 'max_change': 207.33486215505422, 'min_val': -194.7778404059706, 'max_val': 207.33139455351935, 'mean_val': -0.0005131324601765073, 'std_val': 5.933794257239897}, 2.0: {'has_changes': True, 'avg_change': 1.479307295791412, 'max_change': 577.9950625055357, 'min_val': -596.4213034716093, 'max_val': 365.71307818454477, 'mean_val': 0.018845978566698823, 'std_val': 12.149667884721243}}, simulation_steps_results: {1: {'avg_step_time': 0.0011372566223144531, 'metrics': {'timestamp': '2025-05-13T03:33:08.021040', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0006754398345947266, 'metrics': {'timestamp': '2025-05-13T03:33:08.024525', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.000584721565246582, 'metrics': {'timestamp': '2025-05-13T03:33:08.030404', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 1.625487897344789e-07, 'max_curvature': 0.00018604711189647123, 'min_curvature': -0.00022695649128277014, 'std_deviation': 2.0719705316014492e-05, 'total_energy': 0.09497805846785264, 'quantum_density': 7.345534664441196e+29}}} |
| Test 4 | ✅ Réussi | 0.0735 | initialization_ok: True, shape_ok: True, expected_shape: (4, 32, 32, 32), actual_shape: (4, 32, 32, 32), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 1.4999034830736298, 'max_change': 163.57430146440532, 'min_val': -105.91857228394593, 'max_val': 163.57430146440532, 'mean_val': 0.005082459605059238, 'std_val': 5.314730479299912}, 1.0: {'has_changes': True, 'avg_change': 2.966445449904547, 'max_change': 301.734306071234, 'min_val': -299.63232114298813, 'max_val': 289.55049987302897, 'mean_val': 0.022065494708902827, 'std_val': 11.73066640462572}, 2.0: {'has_changes': True, 'avg_change': 5.963061224519519, 'max_change': 690.8139647585162, 'min_val': -654.4758513361675, 'max_val': 484.4969708957325, 'mean_val': 0.10350137249495325, 'std_val': 24.224734744066556}}, simulation_steps_results: {1: {'avg_step_time': 0.0026369094848632812, 'metrics': {'timestamp': '2025-05-13T03:33:08.071881', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0027343273162841798, 'metrics': {'timestamp': '2025-05-13T03:33:08.085556', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': -9.48954593802973e-08, 'max_curvature': 0.00030080881419661894, 'min_curvature': -0.0003057219380321582, 'std_deviation': 2.1526592203188137e-05, 'total_energy': 0.39716912270273486, 'quantum_density': 7.499212406309566e+29}}, 10: {'avg_step_time': 0.0018263816833496093, 'metrics': {'timestamp': '2025-05-13T03:33:08.103874', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 6.224580347168632e-08, 'max_curvature': 0.00032206314601841154, 'min_curvature': -0.0002539430613500451, 'std_deviation': 4.2267011490717036e-05, 'total_energy': 0.9837254684917184, 'quantum_density': 1.8574370000150536e+30}}} |
| Test 5 | ✅ Réussi | 0.0787 | initialization_ok: True, shape_ok: True, expected_shape: (8, 32, 32, 32), actual_shape: (8, 32, 32, 32), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.7561743647267943, 'max_change': 152.94567374078403, 'min_val': -152.94567374078403, 'max_val': 139.49490342062938, 'mean_val': -0.0030305638833689787, 'std_val': 3.823743470676431}, 1.0: {'has_changes': True, 'avg_change': 1.5223057523984305, 'max_change': 258.1905411725164, 'min_val': -260.49153720800894, 'max_val': 225.01131746059798, 'mean_val': 0.005070089659587269, 'std_val': 8.52674449782394}, 2.0: {'has_changes': True, 'avg_change': 3.0179910880677525, 'max_change': 633.0758051983826, 'min_val': -621.5242195078647, 'max_val': 564.8473001194868, 'mean_val': 0.032607680464271545, 'std_val': 17.25476064791924}}, simulation_steps_results: {1: {'avg_step_time': 0.0029935836791992188, 'metrics': {'timestamp': '2025-05-13T03:33:08.131582', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.006357812881469726, 'metrics': {'timestamp': '2025-05-13T03:33:08.163369', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.0019103050231933593, 'metrics': {'timestamp': '2025-05-13T03:33:08.182502', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 2.294900551760807e-07, 'max_curvature': 0.0003155163120201001, 'min_curvature': -0.00032680313518010894, 'std_deviation': 3.0149538497378554e-05, 'total_energy': 0.6403030484204781, 'quantum_density': 1.2089984568378986e+30}}} |
| Test 6 | ✅ Réussi | 0.0921 | initialization_ok: True, shape_ok: True, expected_shape: (16, 32, 32, 32), actual_shape: (16, 32, 32, 32), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.36765807116468907, 'max_change': 132.5420317608815, 'min_val': -132.5420317608815, 'max_val': 96.74341204278531, 'mean_val': -0.0101077709111615, 'std_val': 2.6016589465572846}, 1.0: {'has_changes': True, 'avg_change': 0.7533176388423204, 'max_change': 254.66604777804378, 'min_val': -254.92786166328221, 'max_val': 296.3525171172426, 'mean_val': -0.006749886675805012, 'std_val': 6.010549166179521}, 2.0: {'has_changes': True, 'avg_change': 1.5068277738166431, 'max_change': 632.3018125679038, 'min_val': -477.5106213174163, 'max_val': 621.6413177156544, 'mean_val': 0.004619024332192698, 'std_val': 12.286152437721604}}, simulation_steps_results: {1: {'avg_step_time': 0.002474546432495117, 'metrics': {'timestamp': '2025-05-13T03:33:08.224971', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.001957273483276367, 'metrics': {'timestamp': '2025-05-13T03:33:08.234781', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.003978848457336426, 'metrics': {'timestamp': '2025-05-13T03:33:08.274560', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -4.725710739358972e-10, 'max_curvature': 0.00021970549032400912, 'min_curvature': -0.00025133594107545735, 'std_deviation': 2.100396251185483e-05, 'total_energy': 0.39018468274704177, 'quantum_density': 7.367334584563437e+29}}} |
| Test 7 | ✅ Réussi | 0.1559 | initialization_ok: True, shape_ok: True, expected_shape: (4, 50, 50, 50), actual_shape: (4, 50, 50, 50), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 1.4980661806966813, 'max_change': 150.70586640702945, 'min_val': -149.15753032344932, 'max_val': 150.70586640702945, 'mean_val': -0.008330645480258277, 'std_val': 5.319519304138818}, 1.0: {'has_changes': True, 'avg_change': 2.995424438714083, 'max_change': 319.9844541537004, 'min_val': -319.05179785991623, 'max_val': 298.9589852998951, 'mean_val': -0.0017670605639674081, 'std_val': 11.870756760998065}, 2.0: {'has_changes': True, 'avg_change': 5.9882439436837265, 'max_change': 539.0225129531503, 'min_val': -511.61202797919435, 'max_val': 540.4206114404161, 'mean_val': 0.006296704601474491, 'std_val': 24.1920770371678}}, simulation_steps_results: {1: {'avg_step_time': 0.00901484489440918, 'metrics': {'timestamp': '2025-05-13T03:33:08.313913', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.009018325805664062, 'metrics': {'timestamp': '2025-05-13T03:33:08.358989', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 4.696569684003811e-08, 'max_curvature': 0.0004021760296309262, 'min_curvature': -0.00029818960866007284, 'std_deviation': 2.115962650237389e-05, 'total_energy': 1.4942655283723427, 'quantum_density': 7.396186892746783e+29}}, 10: {'avg_step_time': 0.007098674774169922, 'metrics': {'timestamp': '2025-05-13T03:33:08.430090', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 1.3340453145115983e-07, 'max_curvature': 0.00039989566746248165, 'min_curvature': -0.0004756728067722533, 'std_deviation': 4.250942492941345e-05, 'total_energy': 3.758762466243637, 'quantum_density': 1.860479891820967e+30}}} |
| Test 8 | ✅ Réussi | 0.1656 | initialization_ok: True, shape_ok: True, expected_shape: (8, 50, 50, 50), actual_shape: (8, 50, 50, 50), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.7449491926218035, 'max_change': 167.36740806608208, 'min_val': -167.36740806608208, 'max_val': 134.44295923896556, 'mean_val': -0.0014028800552947655, 'std_val': 3.7340106733016176}, 1.0: {'has_changes': True, 'avg_change': 1.5009469687677224, 'max_change': 407.76892537639867, 'min_val': -406.72059658182627, 'max_val': 324.4959680965349, 'mean_val': 0.011483333380517257, 'std_val': 8.409465662230767}, 2.0: {'has_changes': True, 'avg_change': 3.0034898119123765, 'max_change': 602.7265062625316, 'min_val': -584.0881753321031, 'max_val': 573.7379894437979, 'mean_val': 0.0353811020884901, 'std_val': 17.23871798655994}}, simulation_steps_results: {1: {'avg_step_time': 0.006836414337158203, 'metrics': {'timestamp': '2025-05-13T03:33:08.501912', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0065310955047607425, 'metrics': {'timestamp': '2025-05-13T03:33:08.534603', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.006113958358764648, 'metrics': {'timestamp': '2025-05-13T03:33:08.595895', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 1.488743855846197e-07, 'max_curvature': 0.00038987631322789885, 'min_curvature': -0.00032986381086476396, 'std_deviation': 3.0091739520704504e-05, 'total_energy': 2.4384117562052947, 'quantum_density': 1.2069440623454775e+30}}} |
| Test 9 | ✅ Réussi | 0.2433 | initialization_ok: True, shape_ok: True, expected_shape: (16, 50, 50, 50), actual_shape: (16, 50, 50, 50), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.3747382427593421, 'max_change': 181.4514533038627, 'min_val': -158.70833344173855, 'max_val': 181.4514533038627, 'mean_val': -0.00019018073323743661, 'std_val': 2.6697962862651803}, 1.0: {'has_changes': True, 'avg_change': 0.7458156450569333, 'max_change': 328.009668821592, 'min_val': -326.90023788070806, 'max_val': 316.58010691459884, 'mean_val': 6.70030955399468e-05, 'std_val': 5.895835865297616}, 2.0: {'has_changes': True, 'avg_change': 1.49411890327757, 'max_change': 564.174847867732, 'min_val': -575.9215067639028, 'max_val': 607.3607692578997, 'mean_val': 0.003571716682328876, 'std_val': 12.138377743359982}}, simulation_steps_results: {1: {'avg_step_time': 0.008429288864135742, 'metrics': {'timestamp': '2025-05-13T03:33:08.711006', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.008572530746459962, 'metrics': {'timestamp': '2025-05-13T03:33:08.753826', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.00851442813873291, 'metrics': {'timestamp': '2025-05-13T03:33:08.839061', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 3.306904942729929e-08, 'max_curvature': 0.0002911392561440866, 'min_curvature': -0.0003675351620586043, 'std_deviation': 2.112075574155164e-05, 'total_energy': 1.4944429329652646, 'quantum_density': 7.397064994730647e+29}}} |

### ✅ Neurone Quantique

- **Tests**: 1
- **Réussis**: 1
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 0.0215 | initialization_ok: True, activation_tests: {'0.0': -0.012646256201462203, '0.5': -0.010850734395630335, '1.0': -0.009087769238675047, '-0.5': -0.014544855325006267, '-1.0': -0.01660564725606606}, learning_tests: {'epochs': 100, 'learning_rate': 0.1, 'final_error': -0.002273174305443104, 'error_reduction': 0.5084936597395548, 'final_results': {'0.0->0.0': {'output': 0.5262135167843434, 'error': 0.5262135167843434}, '0.0->1.0': {'output': 0.5228647416662704, 'error': 0.4771352583337296}, '1.0->0.0': {'output': 0.5650466077941122, 'error': 0.5650466077941122}, '1.0->1.0': {'output': 0.5662790233970834, 'error': 0.43372097660291664}}} |

### ❌ Réseau P2P

- **Tests**: 1
- **Réussis**: 0
- **Échoués**: 1
- **Ignorés**: 0
- **Taux de réussite**: 0.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ❌ Échoué | 0.0001 | error: 'P2PNetwork' object has no attribute 'port' |

### ✅ Mécanisme de Consensus

- **Tests**: 1
- **Réussis**: 1
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 0.0018 | initialization_ok: True, validation_tests: {'request_created': True, 'request_content': "{'request_id': '1d0d5790b0f06293', 'item_id': 'test_item_001', 'item_type': 'SOLUTION', 'item_data': {'content': 'Test solution data'}, 'requester_id': 'test_node', 'validator_id': 'validator_001', 'timestamp': 1747107188.8718832, 'criteria': ['consistency', 'correctness', 'completeness', 'efficiency']}", 'request_processed': True, 'result': '<core.consensus.proof_of_cognition.ValidationResult object at 0x7f8e567aea10>'}, validator_tests: {'validators_selected': True, 'validator_count': 0, 'validators': '[]'} |

### ✅ Visualisation

- **Tests**: 1
- **Réussis**: 1
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 0.5708 | initialization_ok: True, visualization_tests: {'plot_3d': {'error': 'too many values to unpack (expected 3)'}, 'plot_2d': {'error': 'Invalid shape (32, 32, 32) for image data'}} |

### ✅ Gestionnaire d'Export

- **Tests**: 1
- **Réussis**: 1
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 0.0304 | initialization_ok: True, export_tests: {'excel': {'error': "No module named 'openpyxl'"}, 'hdf5': {'export_successful': True}, 'csv': {'error': 'too many values to unpack (expected 3)'}} |

### ✅ Gestionnaire de Base de Données

- **Tests**: 1
- **Réussis**: 0
- **Échoués**: 0
- **Ignorés**: 1
- **Taux de réussite**: 0.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ⚠️ Ignoré | 0.0000 | error: Module non disponible |

## Métriques de Performance

### Simulateur

| Métrique | Valeur |
|----------|-------|
| init_times | {20: 0.0004646778106689453, 32: 0.0005965232849121094, 50: 0.0005891323089599609, 64: 0.0045053958892822266} |
| fluctuation_times | {20: 0.0004448890686035156, 32: 0.0022335052490234375, 50: 0.006001949310302734, 64: 0.015218019485473633} |
| simulation_step_times | {20: {'min': 0.0007257461547851562, 'max': 0.0009589195251464844, 'avg': 0.0008042335510253906}, 32: {'min': 0.0023071765899658203, 'max': 0.01740741729736328, 'avg': 0.005350828170776367}, 50: {'min': 0.005961418151855469, 'max': 0.00643610954284668, 'avg': 0.0062163352966308595}, 64: {'min': 0.012463092803955078, 'max': 0.03239130973815918, 'avg': 0.016983556747436523}} |
| memory_usage_mb | {20: 0.0, 32: 0.0, 50: 0.0, 64: 0.125} |

## Conclusion

Le système Neurax a passé une bonne partie des tests avec succès. Quelques améliorations sont nécessaires, mais le système est fonctionnel.

---

*Rapport généré automatiquement par le Framework de Test Neurax*
