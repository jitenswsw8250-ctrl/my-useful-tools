package com.example.ui.tools

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp

@Composable
fun BmiCalculatorScreen(modifier: Modifier = Modifier) {
  var heightStr by rememberSaveable { mutableStateOf("170") }
  var weightStr by rememberSaveable { mutableStateOf("65") }
  var bmiResult by rememberSaveable { mutableStateOf<String?>(null) }
  var categoryResult by rememberSaveable { mutableStateOf<String?>(null) }

  fun calculate() {
    val h = heightStr.toDoubleOrNull() ?: 0.0
    val w = weightStr.toDoubleOrNull() ?: 0.0
    if (h > 0 && w > 0) {
      val hMeters = h / 100.0
      val bmi = w / (hMeters * hMeters)
      bmiResult = String.format("%.1f", bmi)
      categoryResult = when {
        bmi < 18.5 -> "Underweight"
        bmi < 25.0 -> "Normal weight"
        bmi < 30.0 -> "Overweight"
        else -> "Obese"
      }
    }
  }

  Column(modifier = modifier.fillMaxWidth().padding(16.dp)) {
    Card(
      shape = RoundedCornerShape(16.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      modifier = Modifier.fillMaxWidth()
    ) {
      Column(modifier = Modifier.padding(20.dp)) {
        Text("BMI Calculator", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
        Spacer(modifier = Modifier.height(12.dp))
        OutlinedTextField(
          value = heightStr,
          onValueChange = { heightStr = it },
          label = { Text("Height (cm)") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          modifier = Modifier.fillMaxWidth().testTag("bmi_height_input")
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
          value = weightStr,
          onValueChange = { weightStr = it },
          label = { Text("Weight (kg)") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          modifier = Modifier.fillMaxWidth().testTag("bmi_weight_input")
        )
        Spacer(modifier = Modifier.height(12.dp))
        Button(
          onClick = { calculate() },
          modifier = Modifier.fillMaxWidth().testTag("bmi_calculate_button")
        ) {
          Text("Calculate BMI")
        }

        if (bmiResult != null) {
          Spacer(modifier = Modifier.height(16.dp))
          Text("BMI: ${bmiResult} (${categoryResult})", fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
        }
      }
    }
  }
}
