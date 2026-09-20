package com.example.ui.tools

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ui.components.AdSensePlaceholder
import com.example.ui.theme.Amber600
import com.example.ui.theme.Emerald600
import com.example.ui.theme.Rose600

@Composable
fun BmiCalculatorScreen(modifier: Modifier = Modifier) {
  var isMetric by rememberSaveable { mutableStateOf(true) }

  // Metric values
  var heightCmStr by rememberSaveable { mutableStateOf("175") }
  var weightKgStr by rememberSaveable { mutableStateOf("70") }

  // Imperial values
  var heightFeetStr by rememberSaveable { mutableStateOf("5") }
  var heightInchesStr by rememberSaveable { mutableStateOf("9") }
  var weightLbsStr by rememberSaveable { mutableStateOf("154") }

  val bmiResult by remember {
    derivedStateOf {
      val heightInMeters: Double
      val weightInKg: Double

      if (isMetric) {
        val cm = heightCmStr.toDoubleOrNull() ?: 0.0
        val kg = weightKgStr.toDoubleOrNull() ?: 0.0
        heightInMeters = cm / 100.0
        weightInKg = kg
      } else {
        val ft = heightFeetStr.toDoubleOrNull() ?: 0.0
        val inches = heightInchesStr.toDoubleOrNull() ?: 0.0
        val totalInches = (ft * 12.0) + inches
        val lbs = weightLbsStr.toDoubleOrNull() ?: 0.0
        heightInMeters = totalInches * 0.0254
        weightInKg = lbs * 0.45359237
      }

      if (heightInMeters <= 0.5 || weightInKg <= 10.0) {
        null
      } else {
        val bmi = weightInKg / (heightInMeters * heightInMeters)
        val category = when {
          bmi < 18.5 -> BmiCategory.UNDERWEIGHT
          bmi < 25.0 -> BmiCategory.NORMAL
          bmi < 30.0 -> BmiCategory.OVERWEIGHT
          else -> BmiCategory.OBESE
        }

        val healthyMinKg = 18.5 * (heightInMeters * heightInMeters)
        val healthyMaxKg = 24.9 * (heightInMeters * heightInMeters)

        BmiCalculation(
          bmi = bmi,
          category = category,
          healthyMinKg = healthyMinKg,
          healthyMaxKg = healthyMaxKg,
          healthyMinLbs = healthyMinKg / 0.45359237,
          healthyMaxLbs = healthyMaxKg / 0.45359237,
          isMetric = isMetric
        )
      }
    }
  }

  Column(
    modifier = modifier
      .fillMaxWidth()
      .padding(16.dp)
  ) {
    Text(
      text = "BMI Calculator",
      style = MaterialTheme.typography.headlineMedium,
      fontWeight = FontWeight.Bold,
      color = MaterialTheme.colorScheme.onBackground
    )
    Text(
      text = "Calculate your Body Mass Index (BMI) to understand your body weight classification and ideal healthy weight range.",
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      modifier = Modifier.padding(top = 4.dp, bottom = 12.dp)
    )

    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - BMI Tool Top")

    Card(
      modifier = Modifier
        .fillMaxWidth()
        .padding(vertical = 8.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
      shape = RoundedCornerShape(16.dp)
    ) {
      Column(modifier = Modifier.padding(16.dp)) {
        // Unit Switcher: Metric vs Imperial
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.SpaceBetween,
          verticalAlignment = Alignment.CenterVertically
        ) {
          Text(
            text = "Measurements",
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.SemiBold
          )

          Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
            FilterChip(
              selected = isMetric,
              onClick = { isMetric = true },
              label = { Text("Metric (cm / kg)") },
              modifier = Modifier.testTag("metric_chip")
            )
            FilterChip(
              selected = !isMetric,
              onClick = { isMetric = false },
              label = { Text("Imperial (ft / lbs)") },
              modifier = Modifier.testTag("imperial_chip")
            )
          }
        }

        Spacer(modifier = Modifier.height(16.dp))

        if (isMetric) {
          // Metric Inputs
          OutlinedTextField(
            value = heightCmStr,
            onValueChange = { heightCmStr = it },
            label = { Text("Height (cm)") },
            placeholder = { Text("e.g. 175") },
            trailingIcon = { Text("cm", fontWeight = FontWeight.Bold, modifier = Modifier.padding(end = 12.dp)) },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
            singleLine = true,
            modifier = Modifier
              .fillMaxWidth()
              .testTag("height_cm_input")
          )

          Spacer(modifier = Modifier.height(12.dp))

          OutlinedTextField(
            value = weightKgStr,
            onValueChange = { weightKgStr = it },
            label = { Text("Weight (kg)") },
            placeholder = { Text("e.g. 70") },
            trailingIcon = { Text("kg", fontWeight = FontWeight.Bold, modifier = Modifier.padding(end = 12.dp)) },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
            singleLine = true,
            modifier = Modifier
              .fillMaxWidth()
              .testTag("weight_kg_input")
          )
        } else {
          // Imperial Inputs
          Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
          ) {
            OutlinedTextField(
              value = heightFeetStr,
              onValueChange = { heightFeetStr = it },
              label = { Text("Height (ft)") },
              placeholder = { Text("e.g. 5") },
              trailingIcon = { Text("ft", fontWeight = FontWeight.Bold) },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
              singleLine = true,
              modifier = Modifier
                .weight(1f)
                .testTag("height_ft_input")
            )

            OutlinedTextField(
              value = heightInchesStr,
              onValueChange = { heightInchesStr = it },
              label = { Text("Inches (in)") },
              placeholder = { Text("e.g. 9") },
              trailingIcon = { Text("in", fontWeight = FontWeight.Bold) },
              keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
              singleLine = true,
              modifier = Modifier
                .weight(1f)
                .testTag("height_in_input")
            )
          }

          Spacer(modifier = Modifier.height(12.dp))

          OutlinedTextField(
            value = weightLbsStr,
            onValueChange = { weightLbsStr = it },
            label = { Text("Weight (lbs)") },
            placeholder = { Text("e.g. 154") },
            trailingIcon = { Text("lbs", fontWeight = FontWeight.Bold, modifier = Modifier.padding(end = 12.dp)) },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
            singleLine = true,
            modifier = Modifier
              .fillMaxWidth()
              .testTag("weight_lbs_input")
          )
        }

        Spacer(modifier = Modifier.height(20.dp))

        // Action Buttons
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
          Button(
            onClick = { /* reactive recalculation triggers automatically */ },
            modifier = Modifier
              .weight(1f)
              .height(48.dp)
              .testTag("calculate_bmi_button")
          ) {
            Icon(Icons.Default.Favorite, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Calculate BMI")
          }

          OutlinedButton(
            onClick = {
              if (isMetric) {
                heightCmStr = ""
                weightKgStr = ""
              } else {
                heightFeetStr = ""
                heightInchesStr = ""
                weightLbsStr = ""
              }
            },
            modifier = Modifier
              .height(48.dp)
              .testTag("clear_bmi_button")
          ) {
            Icon(Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Clear")
          }
        }
      }
    }

    // Results Box
    bmiResult?.let { result ->
      Spacer(modifier = Modifier.height(16.dp))

      Card(
        modifier = Modifier
          .fillMaxWidth()
          .testTag("bmi_result_card"),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
        shape = RoundedCornerShape(16.dp)
      ) {
        Column(
          modifier = Modifier.padding(20.dp),
          horizontalAlignment = Alignment.CenterHorizontally
        ) {
          Text(
            text = "YOUR BODY MASS INDEX",
            style = MaterialTheme.typography.labelMedium,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.onPrimaryContainer.copy(alpha = 0.8f),
            letterSpacing = 1.2.sp
          )

          Spacer(modifier = Modifier.height(4.dp))

          Text(
            text = "%.1f".format(result.bmi),
            style = MaterialTheme.typography.displayMedium,
            fontWeight = FontWeight.Black,
            color = result.category.color
          )

          // Category Badge
          Box(
            modifier = Modifier
              .clip(RoundedCornerShape(20.dp))
              .background(result.category.color.copy(alpha = 0.15f))
              .padding(horizontal = 16.dp, vertical = 6.dp)
          ) {
            Text(
              text = result.category.label,
              style = MaterialTheme.typography.titleMedium,
              fontWeight = FontWeight.Bold,
              color = result.category.color
            )
          }

          Spacer(modifier = Modifier.height(16.dp))

          // Visual Gauge Bar
          Column(
            modifier = Modifier
              .fillMaxWidth()
              .clip(RoundedCornerShape(12.dp))
              .background(MaterialTheme.colorScheme.surface)
              .padding(14.dp)
          ) {
            Text(
              text = "BMI Spectrum",
              style = MaterialTheme.typography.titleSmall,
              fontWeight = FontWeight.Bold
            )

            Spacer(modifier = Modifier.height(8.dp))

            // 4 Segment Color Bar
            Row(
              modifier = Modifier
                .fillMaxWidth()
                .height(12.dp)
                .clip(RoundedCornerShape(6.dp))
            ) {
              Box(modifier = Modifier.weight(18.5f).fillMaxHeight().background(Amber600))
              Box(modifier = Modifier.weight(6.4f).fillMaxHeight().background(Emerald600))
              Box(modifier = Modifier.weight(5f).fillMaxHeight().background(Color(0xFFEA580C)))
              Box(modifier = Modifier.weight(10f).fillMaxHeight().background(Rose600))
            }

            Spacer(modifier = Modifier.height(6.dp))

            Row(
              modifier = Modifier.fillMaxWidth(),
              horizontalArrangement = Arrangement.SpaceBetween
            ) {
              Text("<18.5\nUnder", style = MaterialTheme.typography.labelSmall, fontSize = 9.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
              Text("18.5-24.9\nNormal", style = MaterialTheme.typography.labelSmall, fontSize = 9.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
              Text("25-29.9\nOver", style = MaterialTheme.typography.labelSmall, fontSize = 9.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
              Text("30+\nObese", style = MaterialTheme.typography.labelSmall, fontSize = 9.sp, color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
          }

          Spacer(modifier = Modifier.height(14.dp))

          // Healthy Weight Advice
          Box(
            modifier = Modifier
              .fillMaxWidth()
              .clip(RoundedCornerShape(12.dp))
              .background(MaterialTheme.colorScheme.surface)
              .padding(14.dp)
          ) {
            Column {
              Text(
                text = "Healthy Weight Range For Your Height",
                style = MaterialTheme.typography.labelMedium,
                fontWeight = FontWeight.Bold,
                color = MaterialTheme.colorScheme.onSurface
              )
              Spacer(modifier = Modifier.height(4.dp))
              Text(
                text = if (result.isMetric) {
                  "%.1f kg – %.1f kg".format(result.healthyMinKg, result.healthyMaxKg)
                } else {
                  "%.1f lbs – %.1f lbs".format(result.healthyMinLbs, result.healthyMaxLbs)
                },
                style = MaterialTheme.typography.titleMedium,
                fontWeight = FontWeight.Bold,
                color = Emerald600
              )
            }
          }
        }
      }
    }

    Spacer(modifier = Modifier.height(16.dp))
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - BMI Tool Bottom")
  }
}

enum class BmiCategory(val label: String, val color: Color) {
  UNDERWEIGHT("Underweight", Amber600),
  NORMAL("Normal Weight", Emerald600),
  OVERWEIGHT("Overweight", Color(0xFFEA580C)),
  OBESE("Obese", Rose600)
}

data class BmiCalculation(
  val bmi: Double,
  val category: BmiCategory,
  val healthyMinKg: Double,
  val healthyMaxKg: Double,
  val healthyMinLbs: Double,
  val healthyMaxLbs: Double,
  val isMetric: Boolean
)
