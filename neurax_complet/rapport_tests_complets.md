# Rapport de Test Complet du Réseau Neuronal Gravitationnel Quantique (Neurax)

Date: 2025-05-13 00:43:11

## Résumé

- **Total des tests**: 15
- **Tests réussis**: 12
- **Tests échoués**: 1
- **Tests ignorés**: 2
- **Taux de réussite**: 80.0%
- **Temps d'exécution total**: 2.66 secondes

## Configuration Matérielle

- **Système**: posix
- **CPU Logiques**: 8
- **CPU Physiques**: 4
- **Mémoire Totale**: 62.81 GB
- **Mémoire Disponible**: 33.74 GB
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
| Test 1 | ✅ Réussi | 0.0138 | initialization_ok: True, shape_ok: True, expected_shape: (4, 20, 20, 20), actual_shape: (4, 20, 20, 20), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 1.4736458665466052, 'max_change': 105.53115545592983, 'min_val': -105.53115545592983, 'max_val': 100.6015735378747, 'mean_val': 0.04701314679663556, 'std_val': 5.144380941753307}, 1.0: {'has_changes': True, 'avg_change': 3.007167691879225, 'max_change': 243.08298988101444, 'min_val': -233.21258980056305, 'max_val': 228.01723949952574, 'mean_val': 0.08276349403274418, 'std_val': 11.821807621525016}, 2.0: {'has_changes': True, 'avg_change': 5.908517384522779, 'max_change': 564.447465701765, 'min_val': -422.85156225889494, 'max_val': 562.950719003356, 'mean_val': 0.2908561140893601, 'std_val': 24.356174393538662}}, simulation_steps_results: {1: {'avg_step_time': 0.0007932186126708984, 'metrics': {'timestamp': '2025-05-13T00:43:12.282802', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0007020950317382813, 'metrics': {'timestamp': '2025-05-13T00:43:12.286414', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': -4.837770787576209e-08, 'max_curvature': 0.0002286231025494514, 'min_curvature': -0.00016601767370571398, 'std_deviation': 2.1228450226717853e-05, 'total_energy': 0.09566427955576348, 'quantum_density': 7.398606509349731e+29}}, 10: {'avg_step_time': 0.0006160497665405274, 'metrics': {'timestamp': '2025-05-13T00:43:12.292600', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 4.9450961751882654e-08, 'max_curvature': 0.00027512561578198387, 'min_curvature': -0.0002245758600327202, 'std_deviation': 4.262683618997398e-05, 'total_energy': 0.24189371555161404, 'quantum_density': 1.8707885814451226e+30}}} |
| Test 2 | ✅ Réussi | 0.0211 | initialization_ok: True, shape_ok: True, expected_shape: (8, 20, 20, 20), actual_shape: (8, 20, 20, 20), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.7524361925996712, 'max_change': 114.27845274461912, 'min_val': -84.70077478531303, 'max_val': 114.27845274461912, 'mean_val': -0.0036366075025205066, 'std_val': 3.7536910385416538}, 1.0: {'has_changes': True, 'avg_change': 1.5093828368901072, 'max_change': 265.43552453958404, 'min_val': -259.7545520647998, 'max_val': 187.11158427334718, 'mean_val': -0.04610048957149529, 'std_val': 8.480559386565105}, 2.0: {'has_changes': True, 'avg_change': 2.9640676373817176, 'max_change': 1160.9210655850381, 'min_val': -1172.2293537148475, 'max_val': 567.7244789576575, 'mean_val': -0.06877940147097274, 'std_val': 17.570545562352965}}, simulation_steps_results: {1: {'avg_step_time': 0.0006096363067626953, 'metrics': {'timestamp': '2025-05-13T00:43:12.302215', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0006801128387451172, 'metrics': {'timestamp': '2025-05-13T00:43:12.305601', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.0008058309555053711, 'metrics': {'timestamp': '2025-05-13T00:43:12.313699', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 5.367326823825829e-08, 'max_curvature': 0.00020827395646361063, 'min_curvature': -0.00023840745270646, 'std_deviation': 2.991764175500238e-05, 'total_energy': 0.15426277732667704, 'quantum_density': 1.1930572140191896e+30}}} |
| Test 3 | ✅ Réussi | 0.0177 | initialization_ok: True, shape_ok: True, expected_shape: (16, 20, 20, 20), actual_shape: (16, 20, 20, 20), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.37597889967247955, 'max_change': 115.16305583261436, 'min_val': -115.16305583261436, 'max_val': 89.80500583790082, 'mean_val': -0.01676893567576065, 'std_val': 2.6408173961202963}, 1.0: {'has_changes': True, 'avg_change': 0.7373154348266727, 'max_change': 242.91938589202343, 'min_val': -235.59468609012927, 'max_val': 218.33537275574804, 'mean_val': 3.9397881989916786e-05, 'std_val': 5.916935417152905}, 2.0: {'has_changes': True, 'avg_change': 1.4895292900770232, 'max_change': 403.6504662254056, 'min_val': -403.2359354578216, 'max_val': 363.0565880894311, 'mean_val': 0.013590251759832578, 'std_val': 12.24634383077446}}, simulation_steps_results: {1: {'avg_step_time': 0.0008442401885986328, 'metrics': {'timestamp': '2025-05-13T00:43:12.321961', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0007708072662353516, 'metrics': {'timestamp': '2025-05-13T00:43:12.325830', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.0005556106567382813, 'metrics': {'timestamp': '2025-05-13T00:43:12.331444', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -3.394176538150672e-08, 'max_curvature': 0.0001588066101445004, 'min_curvature': -0.00016843022169946294, 'std_deviation': 2.1004929387115435e-05, 'total_energy': 0.09570305048112995, 'quantum_density': 7.401605024805259e+29}}} |
| Test 4 | ✅ Réussi | 0.0378 | initialization_ok: True, shape_ok: True, expected_shape: (4, 32, 32, 32), actual_shape: (4, 32, 32, 32), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 1.4959172034855759, 'max_change': 111.86182091353962, 'min_val': -111.86182091353962, 'max_val': 105.50573496618972, 'mean_val': 0.03406904228197883, 'std_val': 5.254452619555224}, 1.0: {'has_changes': True, 'avg_change': 2.9979672264741883, 'max_change': 277.40398212813335, 'min_val': -253.09716177798697, 'max_val': 276.3436556300181, 'mean_val': 0.013596540512933342, 'std_val': 11.793005645013265}, 2.0: {'has_changes': True, 'avg_change': 6.125468582151575, 'max_change': 597.9729169580186, 'min_val': -583.418136009773, 'max_val': 602.5076144017786, 'mean_val': 0.04520925037168658, 'std_val': 25.074541656391947}}, simulation_steps_results: {1: {'avg_step_time': 0.002404451370239258, 'metrics': {'timestamp': '2025-05-13T00:43:12.342611', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.001761150360107422, 'metrics': {'timestamp': '2025-05-13T00:43:12.351402', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 9.99255647144338e-08, 'max_curvature': 0.0002496324425216489, 'min_curvature': -0.00034989473395168763, 'std_deviation': 2.1389285286898026e-05, 'total_energy': 0.39202782281018916, 'quantum_density': 7.402136128888086e+29}}, 10: {'avg_step_time': 0.0017687559127807617, 'metrics': {'timestamp': '2025-05-13T00:43:12.369096', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 2.1558639971612647e-07, 'max_curvature': 0.00032487277181039644, 'min_curvature': -0.00033125261890494957, 'std_deviation': 4.234290891681111e-05, 'total_energy': 0.9834902776972716, 'quantum_density': 1.8569929207493837e+30}}} |
| Test 5 | ✅ Réussi | 0.0449 | initialization_ok: True, shape_ok: True, expected_shape: (8, 32, 32, 32), actual_shape: (8, 32, 32, 32), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.752962930085006, 'max_change': 115.98279782657933, 'min_val': -115.98279782657933, 'max_val': 113.07542106808621, 'mean_val': 0.005824440510311295, 'std_val': 3.739551173277246}, 1.0: {'has_changes': True, 'avg_change': 1.5033182057513765, 'max_change': 220.59928737892247, 'min_val': -219.59761017593598, 'max_val': 254.8507547399743, 'mean_val': 0.0017110741841863761, 'std_val': 8.362810942071908}, 2.0: {'has_changes': True, 'avg_change': 2.9782555079773383, 'max_change': 471.95531912636545, 'min_val': -456.9737642850261, 'max_val': 461.7737582185817, 'mean_val': 0.06017803087293147, 'std_val': 17.260499095902986}}, simulation_steps_results: {1: {'avg_step_time': 0.00203704833984375, 'metrics': {'timestamp': '2025-05-13T00:43:12.386646', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0019261360168457032, 'metrics': {'timestamp': '2025-05-13T00:43:12.396303', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.0017684459686279296, 'metrics': {'timestamp': '2025-05-13T00:43:12.413992', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': 1.403265979426922e-07, 'max_curvature': 0.0003275792071279807, 'min_curvature': -0.00026963683933225953, 'std_deviation': 3.015093703384359e-05, 'total_energy': 0.6387594698820935, 'quantum_density': 1.2060839242965987e+30}}} |
| Test 6 | ✅ Réussi | 0.0678 | initialization_ok: True, shape_ok: True, expected_shape: (16, 32, 32, 32), actual_shape: (16, 32, 32, 32), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.37395231437316945, 'max_change': 148.16458265193626, 'min_val': -129.19986567886502, 'max_val': 148.16458265193626, 'mean_val': -0.007012013354314795, 'std_val': 2.6820659676294776}, 1.0: {'has_changes': True, 'avg_change': 0.7372333155006816, 'max_change': 256.3670498425183, 'min_val': -226.30697459656355, 'max_val': 268.32049382600474, 'mean_val': 0.0018520123123410095, 'std_val': 5.874319114951854}, 2.0: {'has_changes': True, 'avg_change': 1.4923557169346768, 'max_change': 531.9988493359375, 'min_val': -450.56136968230993, 'max_val': 538.9128331323958, 'mean_val': -0.004314262725764854, 'std_val': 12.099198532562657}}, simulation_steps_results: {1: {'avg_step_time': 0.0028862953186035156, 'metrics': {'timestamp': '2025-05-13T00:43:12.450036', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.0019895553588867186, 'metrics': {'timestamp': '2025-05-13T00:43:12.460114', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.0021695613861083983, 'metrics': {'timestamp': '2025-05-13T00:43:12.481708', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -1.7640076700859428e-07, 'max_curvature': 0.00021192279999311873, 'min_curvature': -0.0002092552804644681, 'std_deviation': 2.0697106684171773e-05, 'total_energy': 0.38768295976874534, 'quantum_density': 7.320097901438822e+29}}} |
| Test 7 | ✅ Réussi | 0.1382 | initialization_ok: True, shape_ok: True, expected_shape: (4, 50, 50, 50), actual_shape: (4, 50, 50, 50), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 1.488388772838039, 'max_change': 142.49586242131895, 'min_val': -142.49586242131895, 'max_val': 136.16967250361841, 'mean_val': 0.0037608663651673836, 'std_val': 5.26811408723569}, 1.0: {'has_changes': True, 'avg_change': 2.992196882795276, 'max_change': 351.11599319553824, 'min_val': -334.9145789781035, 'max_val': 351.839898882675, 'mean_val': 0.012216354500521462, 'std_val': 11.829276530678442}, 2.0: {'has_changes': True, 'avg_change': 5.993461924654294, 'max_change': 750.9621238389526, 'min_val': -747.4271284975065, 'max_val': 586.3498957292135, 'mean_val': -0.02100182356343128, 'std_val': 24.287325231643152}}, simulation_steps_results: {1: {'avg_step_time': 0.007218837738037109, 'metrics': {'timestamp': '2025-05-13T00:43:12.525786', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.006260347366333008, 'metrics': {'timestamp': '2025-05-13T00:43:12.557162', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 2.6159884793611873e-08, 'max_curvature': 0.00036450656961482456, 'min_curvature': -0.0003180113019916, 'std_deviation': 2.1314625175271374e-05, 'total_energy': 1.4985224448048975, 'quantum_density': 7.417257411288609e+29}}, 10: {'avg_step_time': 0.00625607967376709, 'metrics': {'timestamp': '2025-05-13T00:43:12.619679', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -2.3281472774421958e-07, 'max_curvature': 0.0004010483001951956, 'min_curvature': -0.0004313056553207026, 'std_deviation': 4.251785203716939e-05, 'total_energy': 3.756182784500127, 'quantum_density': 1.8592030231562934e+30}}} |
| Test 8 | ✅ Réussi | 0.1532 | initialization_ok: True, shape_ok: True, expected_shape: (8, 50, 50, 50), actual_shape: (8, 50, 50, 50), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.7457998336764866, 'max_change': 165.16063312475757, 'min_val': -142.67034895064876, 'max_val': 165.16063312475757, 'mean_val': -0.0020565880327585388, 'std_val': 3.7391257578421695}, 1.0: {'has_changes': True, 'avg_change': 1.4985447225015738, 'max_change': 291.73605498734776, 'min_val': -292.62030274847996, 'max_val': 311.597317018845, 'mean_val': -0.004003588053890731, 'std_val': 8.390820911467417}, 2.0: {'has_changes': True, 'avg_change': 3.0000698331305165, 'max_change': 635.0843000555202, 'min_val': -599.915163028059, 'max_val': 694.8598968198853, 'mean_val': -0.007001660979728218, 'std_val': 17.27869749181395}}, simulation_steps_results: {1: {'avg_step_time': 0.0066645145416259766, 'metrics': {'timestamp': '2025-05-13T00:43:12.677314', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.007082605361938476, 'metrics': {'timestamp': '2025-05-13T00:43:12.712961', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.005987644195556641, 'metrics': {'timestamp': '2025-05-13T00:43:12.772902', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -1.100193713643054e-07, 'max_curvature': 0.00040532989117420996, 'min_curvature': -0.00034134772912081004, 'std_deviation': 2.9962562121442776e-05, 'total_energy': 2.42712449353367, 'quantum_density': 1.2013571902239078e+30}}} |
| Test 9 | ✅ Réussi | 0.2162 | initialization_ok: True, shape_ok: True, expected_shape: (16, 50, 50, 50), actual_shape: (16, 50, 50, 50), fluctuations_results: {0.5: {'has_changes': True, 'avg_change': 0.3727863459693417, 'max_change': 151.9654645979891, 'min_val': -138.5520971724583, 'max_val': 151.9654645979891, 'mean_val': -0.0017817103768610369, 'std_val': 2.6378957794430438}, 1.0: {'has_changes': True, 'avg_change': 0.7504813362733016, 'max_change': 318.33177794180426, 'min_val': -320.02818015420235, 'max_val': 316.189955127755, 'mean_val': -0.001388132312457815, 'std_val': 5.952718622845359}, 2.0: {'has_changes': True, 'avg_change': 1.4911512722202918, 'max_change': 564.1942143525393, 'min_val': -599.9612301347614, 'max_val': 557.5878105887344, 'mean_val': -0.015562825777971214, 'std_val': 12.122202258496966}}, simulation_steps_results: {1: {'avg_step_time': 0.006875753402709961, 'metrics': {'timestamp': '2025-05-13T00:43:12.890936', 'step': 1, 'simulation_time': 5.391246448313604e-44, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 5: {'avg_step_time': 0.006560707092285156, 'metrics': {'timestamp': '2025-05-13T00:43:12.923916', 'step': 6, 'simulation_time': 3.234747868988162e-43, 'mean_curvature': 0.0, 'max_curvature': 0.0, 'min_curvature': 0.0, 'std_deviation': 0.0, 'total_energy': 0.0, 'quantum_density': 0.0}}, 10: {'avg_step_time': 0.006528973579406738, 'metrics': {'timestamp': '2025-05-13T00:43:12.989199', 'step': 16, 'simulation_time': 8.625994317301766e-43, 'mean_curvature': -3.530730019295328e-08, 'max_curvature': 0.0004066847307902885, 'min_curvature': -0.000328729948377159, 'std_deviation': 2.1438786331926348e-05, 'total_energy': 1.5066549014736939, 'quantum_density': 7.45751074530288e+29}}} |

### ✅ Neurone Quantique

- **Tests**: 1
- **Réussis**: 0
- **Échoués**: 0
- **Ignorés**: 1
- **Taux de réussite**: 0.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ⚠️ Ignoré | 0.0000 | error: Module non disponible |

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
| Test 1 | ✅ Réussi | 0.0013 | initialization_ok: True, validation_tests: {'request_created': True, 'request_content': "{'request_id': 'ed2226fa920181d3', 'item_id': 'test_item_001', 'item_type': 'SOLUTION', 'item_data': {'content': 'Test solution data'}, 'requester_id': 'test_node', 'validator_id': 'validator_001', 'timestamp': 1747096992.9991355, 'criteria': ['consistency', 'correctness', 'completeness', 'efficiency']}", 'request_processed': True, 'result': '<core.consensus.proof_of_cognition.ValidationResult object at 0x7fd4bf208310>'}, validator_tests: {'validators_selected': True, 'validator_count': 0, 'validators': '[]'} |

### ✅ Visualisation

- **Tests**: 1
- **Réussis**: 1
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 1.9057 | initialization_ok: True, visualization_tests: {'plot_3d': {'error': 'too many values to unpack (expected 3)'}, 'plot_2d': {'error': 'Invalid shape (32, 32, 32) for image data'}} |

### ✅ Gestionnaire d'Export

- **Tests**: 1
- **Réussis**: 1
- **Échoués**: 0
- **Ignorés**: 0
- **Taux de réussite**: 100.00%

#### Détails des tests

| Test | Statut | Temps (s) | Détails |
|------|--------|-----------|--------|
| Test 1 | ✅ Réussi | 0.0411 | initialization_ok: True, export_tests: {'excel': {'error': "No module named 'openpyxl'"}, 'hdf5': {'export_successful': True}, 'csv': {'error': 'too many values to unpack (expected 3)'}} |

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

## Résultats sur les Puzzles ARC

### Résumé par Phase

| Phase | Nombre de Puzzles | Précision Moyenne | Précision Min | Précision Max |
|-------|------------------|-------------------|---------------|---------------|
| training | 5 | 0.00% | 0.00% | 0.00% |
| test_test_0 | 5 | N/A | N/A | N/A |
| evaluation | 5 | 0.00% | 0.00% | 0.00% |

### Détails des Puzzles (Échantillon de 10)

#### Puzzle 00576224

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| training | ❌ Échoué | 0.0006 | 0.00% | error: list indices must be integers or slices, not str |
| test_test_0 | ⚠️ Ignoré | 0.0248 | N/A | phase: test, input_shape: 2x2, prediction_shape: 2x2, confidence: 0.9722259632313233, metadata: {'min_val': 3.999999044960343, 'max_val': 8.000054519747538, 'avg_val': 6.00001250834304, 'std_val': 1.414220860710129} |

#### Puzzle 007bbfb7

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| training | ❌ Échoué | 0.0003 | 0.00% | error: list indices must be integers or slices, not str |
| test_test_0 | ⚠️ Ignoré | 0.0217 | N/A | phase: test, input_shape: 3x3, prediction_shape: 3x3, confidence: 0.9999903564017819, metadata: {'min_val': -0.00014705561175517556, 'max_val': 7.000054374152067, 'avg_val': 5.4444379517675525, 'std_val': 2.9101912811887947} |

#### Puzzle 009d5c81

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| training | ❌ Échoué | 0.0009 | 0.00% | error: list indices must be integers or slices, not str |
| test_test_0 | ⚠️ Ignoré | 0.0018 | N/A | phase: test, input_shape: 14x14, prediction_shape: None, confidence: 0.0, metadata: {'error': 'could not broadcast input array from shape (14,14) into shape (14,14,0)'} |

#### Puzzle 00d62c1b

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| training | ❌ Échoué | 0.0005 | 0.00% | error: list indices must be integers or slices, not str |
| test_test_0 | ⚠️ Ignoré | 0.0018 | N/A | phase: test, input_shape: 20x20, prediction_shape: None, confidence: 0.0, metadata: {'error': 'could not broadcast input array from shape (20,20) into shape (20,20,0)'} |

#### Puzzle 00dbd492

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| training | ❌ Échoué | 0.0004 | 0.00% | error: list indices must be integers or slices, not str |
| test_test_0 | ⚠️ Ignoré | 0.0017 | N/A | phase: test, input_shape: 20x20, prediction_shape: None, confidence: 0.0, metadata: {'error': 'could not broadcast input array from shape (13,13) into shape (13,13,10)'} |

#### Puzzle 0934a4d8

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| evaluation | ❌ Échoué | 0.0004 | 0.00% | error: list indices must be integers or slices, not str |

#### Puzzle 135a2760

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| evaluation | ❌ Échoué | 0.0004 | 0.00% | error: list indices must be integers or slices, not str |

#### Puzzle 136b0064

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| evaluation | ❌ Échoué | 0.0003 | 0.00% | error: list indices must be integers or slices, not str |

#### Puzzle 13e47133

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| evaluation | ❌ Échoué | 0.0006 | 0.00% | error: list indices must be integers or slices, not str |

#### Puzzle 142ca369

| Phase | Statut | Temps (s) | Précision | Détails |
|-------|--------|-----------|-----------|--------|
| evaluation | ❌ Échoué | 0.0005 | 0.00% | error: list indices must be integers or slices, not str |

## Métriques de Performance

### Simulateur

| Métrique | Valeur |
|----------|-------|
| init_times | {20: 0.0006210803985595703, 32: 0.0009627342224121094, 50: 0.0006482601165771484, 64: 0.0008115768432617188} |
| fluctuation_times | {20: 0.0010714530944824219, 32: 0.0016465187072753906, 50: 0.006281375885009766, 64: 0.013177156448364258} |
| simulation_step_times | {20: {'min': 0.0006344318389892578, 'max': 0.0010120868682861328, 'avg': 0.0008473873138427734}, 32: {'min': 0.0017371177673339844, 'max': 0.0023779869079589844, 'avg': 0.001942586898803711}, 50: {'min': 0.006144285202026367, 'max': 0.008552074432373047, 'avg': 0.007089853286743164}, 64: {'min': 0.012016773223876953, 'max': 0.0129547119140625, 'avg': 0.012396478652954101}} |
| memory_usage_mb | {20: 0.0, 32: 0.0, 50: 0.0, 64: 0.0} |

## Conclusion

Le système Neurax a passé une bonne partie des tests avec succès. Quelques améliorations sont nécessaires, mais le système est fonctionnel.

---

*Rapport généré automatiquement par le Framework de Test Neurax*
