package com.example.ui.tools

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.LocalOffer
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Switch
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
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.ui.components.AdSensePlaceholder
import com.example.ui.theme.Emerald600

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun DiscountCalculatorScreen(modifier: Modifier = Modifier) {
  var originalPriceStr by rememberSaveable { mutableStateOf("120") }
  var discountPercentStr by rememberSaveable { mutableStateOf("25") }
  var enableTax by rememberSaveable { mutableStateOf(false) }
  var taxPercentStr by rememberSaveable { mutableStateOf("8.5") }
  var currencySymbol by rememberSaveable { mutableStateOf("$") }

  val popularDiscounts = listOf(10, 15, 20, 25, 30, 40, 50, 70)

  val discountResult by remember {
    derivedStateOf {
      val price = originalPriceStr.toDoubleOrNull() ?: 0.0
      val discountPct = discountPercentStr.toDoubleOrNull() ?: 0.0
      val taxPct = if (enableTax) (taxPercentStr.toDoubleOrNull() ?: 0.0) else 0.0

      if (price <= 0.0 || discountPct < 0.0) {
        null
      } else {
        val discountAmount = price * (discountPct / 100.0)
        val discountedPrice = (price - discountAmount).coerceAtLeast(0.0)
        val taxAmount = discountedPrice * (taxPct / 100.0)
        val finalPrice = discountedPrice + taxAmount

        DiscountCalculation(
          originalPrice = price,
          discountPercent = discountPct,
          discountAmount = discountAmount,
          discountedPrice = discountedPrice,
          taxAmount = taxAmount,
          finalPrice = finalPrice,
          savingsPercent = if (price > 0) ((price - finalPrice) / price) * 100.0 else 0.0
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
      text = "Discount Calculator",
      style = MaterialTheme.typography.headlineMedium,
      fontWeight = FontWeight.Bold,
      color = MaterialTheme.colorScheme.onBackground
    )
    Text(
      text = "Calculate the final sale price, discount amount saved, and optional sales tax for shopping and retail sales.",
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant,
      modifier = Modifier.padding(top = 4.dp, bottom = 12.dp)
    )

    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Discount Tool Top")

    Card(
      modifier = Modifier
        .fillMaxWidth()
        .padding(vertical = 8.dp),
      colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
      elevation = CardDefaults.cardElevation(defaultElevation = 2.dp),
      shape = RoundedCornerShape(16.dp)
    ) {
      Column(modifier = Modifier.padding(16.dp)) {
        // Currency Selector
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.SpaceBetween,
          verticalAlignment = Alignment.CenterVertically
        ) {
          Text(
            text = "Pricing Information",
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.SemiBold
          )

          Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
            listOf("$", "€", "£", "₹").forEach { symbol ->
              FilterChip(
                selected = currencySymbol == symbol,
                onClick = { currencySymbol = symbol },
                label = { Text(symbol) }
              )
            }
          }
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Original Price Input
        OutlinedTextField(
          value = originalPriceStr,
          onValueChange = { originalPriceStr = it },
          label = { Text("Original Price ($currencySymbol)") },
          placeholder = { Text("e.g. 120.00") },
          leadingIcon = { Text(currencySymbol, fontWeight = FontWeight.Bold) },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          singleLine = true,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("original_price_input")
        )

        Spacer(modifier = Modifier.height(16.dp))

        // Discount Percentage Input
        OutlinedTextField(
          value = discountPercentStr,
          onValueChange = { discountPercentStr = it },
          label = { Text("Discount Percentage (%)") },
          placeholder = { Text("e.g. 25") },
          trailingIcon = { Text("%", fontWeight = FontWeight.Bold, modifier = Modifier.padding(end = 12.dp)) },
          keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
          singleLine = true,
          modifier = Modifier
            .fillMaxWidth()
            .testTag("discount_percent_input")
        )

        Spacer(modifier = Modifier.height(8.dp))

        // Popular Quick Discount Chips
        Text(
          text = "Quick Select:",
          style = MaterialTheme.typography.labelSmall,
          color = MaterialTheme.colorScheme.onSurfaceVariant
        )
        Spacer(modifier = Modifier.height(6.dp))
        FlowRow(
          horizontalArrangement = Arrangement.spacedBy(6.dp),
          verticalArrangement = Arrangement.spacedBy(6.dp),
          modifier = Modifier.fillMaxWidth()
        ) {
          popularDiscounts.forEach { pct ->
            FilterChip(
              selected = discountPercentStr == pct.toString(),
              onClick = { discountPercentStr = pct.toString() },
              label = { Text("$pct%") },
              modifier = Modifier.testTag("discount_chip_$pct")
            )
          }
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Sales Tax Switch Toggle
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.SpaceBetween,
          verticalAlignment = Alignment.CenterVertically
        ) {
          Column {
            Text("Include Sales Tax", style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.Medium)
            Text("Calculate tax on discounted price", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
          }
          Switch(
            checked = enableTax,
            onCheckedChange = { enableTax = it },
            modifier = Modifier.testTag("tax_switch")
          )
        }

        if (enableTax) {
          Spacer(modifier = Modifier.height(12.dp))
          OutlinedTextField(
            value = taxPercentStr,
            onValueChange = { taxPercentStr = it },
            label = { Text("Tax Rate (%)") },
            placeholder = { Text("e.g. 8.5") },
            trailingIcon = { Text("%", fontWeight = FontWeight.Bold, modifier = Modifier.padding(end = 12.dp)) },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Decimal),
            singleLine = true,
            modifier = Modifier
              .fillMaxWidth()
              .testTag("tax_percent_input")
          )
        }

        Spacer(modifier = Modifier.height(20.dp))

        // Buttons
        Row(
          modifier = Modifier.fillMaxWidth(),
          horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
          Button(
            onClick = { /* reactive recalculation triggers automatically */ },
            modifier = Modifier
              .weight(1f)
              .height(48.dp)
              .testTag("calculate_discount_button")
          ) {
            Icon(Icons.Default.LocalOffer, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Calculate Discount")
          }

          OutlinedButton(
            onClick = {
              originalPriceStr = ""
              discountPercentStr = ""
              enableTax = false
            },
            modifier = Modifier
              .height(48.dp)
              .testTag("clear_discount_button")
          ) {
            Icon(Icons.Default.Clear, contentDescription = null, modifier = Modifier.size(18.dp))
            Spacer(modifier = Modifier.width(6.dp))
            Text("Clear")
          }
        }
      }
    }

    // Results Box
    discountResult?.let { result ->
      Spacer(modifier = Modifier.height(16.dp))

      Card(
        modifier = Modifier
          .fillMaxWidth()
          .testTag("discount_result_card"),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
        shape = RoundedCornerShape(16.dp)
      ) {
        Column(
          modifier = Modifier.padding(20.dp),
          horizontalAlignment = Alignment.CenterHorizontally
        ) {
          Text(
            text = "FINAL PRICE TO PAY",
            style = MaterialTheme.typography.labelMedium,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.onPrimaryContainer.copy(alpha = 0.8f),
            letterSpacing = 1.2.sp
          )

          Spacer(modifier = Modifier.height(4.dp))

          Text(
            text = "$currencySymbol %,.2f".format(result.finalPrice),
            style = MaterialTheme.typography.headlineLarge,
            fontWeight = FontWeight.Black,
            color = MaterialTheme.colorScheme.primary
          )

          Spacer(modifier = Modifier.height(16.dp))

          // Savings Banner
          Box(
            modifier = Modifier
              .fillMaxWidth()
              .clip(RoundedCornerShape(12.dp))
              .background(Emerald600.copy(alpha = 0.15f))
              .padding(14.dp),
            contentAlignment = Alignment.Center
          ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
              Text(
                text = "YOU SAVE",
                style = MaterialTheme.typography.labelSmall,
                color = Emerald600,
                fontWeight = FontWeight.Bold,
                letterSpacing = 1.sp
              )
              Text(
                text = "$currencySymbol %,.2f  (%.0f%% OFF)".format(result.discountAmount, result.discountPercent),
                style = MaterialTheme.typography.titleLarge,
                fontWeight = FontWeight.Black,
                color = Emerald600
              )
            }
          }

          Spacer(modifier = Modifier.height(14.dp))

          // Detailed breakdown table
          Column(
            modifier = Modifier
              .fillMaxWidth()
              .clip(RoundedCornerShape(12.dp))
              .background(MaterialTheme.colorScheme.surface)
              .padding(14.dp)
          ) {
            BreakdownRow("Original Price", "$currencySymbol %,.2f".format(result.originalPrice))
            BreakdownRow("Discount Amount", "-$currencySymbol %,.2f".format(result.discountAmount), isDiscount = true)
            BreakdownRow("Price After Discount", "$currencySymbol %,.2f".format(result.discountedPrice))
            if (enableTax) {
              BreakdownRow("Sales Tax ($taxPercentStr%)", "+$currencySymbol %,.2f".format(result.taxAmount))
            }
          }
        }
      }
    }

    Spacer(modifier = Modifier.height(16.dp))
    AdSensePlaceholder(slotLabel = "AdSense Responsive Slot - Discount Tool Bottom")
  }
}

@Composable
private fun BreakdownRow(label: String, value: String, isDiscount: Boolean = false) {
  Row(
    modifier = Modifier
      .fillMaxWidth()
      .padding(vertical = 4.dp),
    horizontalArrangement = Arrangement.SpaceBetween
  ) {
    Text(
      text = label,
      style = MaterialTheme.typography.bodyMedium,
      color = MaterialTheme.colorScheme.onSurfaceVariant
    )
    Text(
      text = value,
      style = MaterialTheme.typography.bodyMedium,
      fontWeight = FontWeight.Bold,
      color = if (isDiscount) Emerald600 else MaterialTheme.colorScheme.onSurface
    )
  }
}

data class DiscountCalculation(
  val originalPrice: Double,
  val discountPercent: Double,
  val discountAmount: Double,
  val discountedPrice: Double,
  val taxAmount: Double,
  val finalPrice: Double,
  val savingsPercent: Double
)
