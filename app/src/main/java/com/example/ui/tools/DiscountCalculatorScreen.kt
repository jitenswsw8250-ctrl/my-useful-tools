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
fun DiscountCalculatorScreen(modifier: Modifier = Modifier) {
  var priceStr by rememberSaveable { mutableStateOf("1000") }
  var discountStr by rememberSaveable { mutableStateOf("20") }
  var finalPriceResult by rememberSaveable { mutableStateOf<String?>(null) }
  var savingsResult by rememberSaveable { mutableStateOf<String?>(null) }

  fun calculate() {
    val price = priceStr.toDoubleOrNull() ?: 0.0
    val discount = discountStr.toDoubleOrNull() ?: 0.0
    if (price >= 0 && discount in 0.0..100.0) {
      val saved = price * (discount / 100.0)
      val finalPrice = price - saved
      savingsResult = String.format("%.2f", saved)
      finalPriceResult = String.format("%.2f", finalPrice)
    }
  }

  Column(modifier = modifier.fillMaxWidth().padding(16.dp)) {
    Card(
      shape = RoundedCornerShape(16.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      modifier = Modifier.fillMaxWidth()
    ) {
      Column(modifier = Modifier.padding(20.dp)) {
        Text("Discount Calculator", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
        Spacer(modifier = Modifier.height(12.dp))
        OutlinedTextField(
          value = priceStr,
          onValueChange = { priceStr = it },
          label = { Text("Original Price") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          modifier = Modifier.fillMaxWidth().testTag("discount_price_input")
        )
        Spacer(modifier = Modifier.height(8.dp))
        OutlinedTextField(
          value = discountStr,
          onValueChange = { discountStr = it },
          label = { Text("Discount (%)") },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          modifier = Modifier.fillMaxWidth().testTag("discount_rate_input")
        )
        Spacer(modifier = Modifier.height(12.dp))
        Button(
          onClick = { calculate() },
          modifier = Modifier.fillMaxWidth().testTag("discount_calculate_button")
        ) {
          Text("Calculate Discount")
        }

        if (finalPriceResult != null) {
          Spacer(modifier = Modifier.height(16.dp))
          Text("Final Price: ₹${finalPriceResult}", fontWeight = FontWeight.Bold, color = MaterialTheme.colorScheme.primary)
          Text("You Save: ₹${savingsResult}", color = MaterialTheme.colorScheme.secondary)
        }
      }
    }
  }
}
